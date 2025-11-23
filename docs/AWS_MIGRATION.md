# BR27 AWS Migration Guide

Complete step-by-step guide to migrate from GitHub Pages to AWS.

---

## 📋 Table of Contents

1. [Pre-Migration Checklist](#pre-migration-checklist)
2. [Option 1: AWS Amplify (Recommended)](#option-1-aws-amplify-recommended)
3. [Option 2: S3 + CloudFront](#option-2-s3--cloudfront)
4. [Option 3: EC2 + Nginx](#option-3-ec2--nginx)
5. [DNS Migration](#dns-migration)
6. [Post-Migration Testing](#post-migration-testing)
7. [Cost Optimization](#cost-optimization)
8. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Pre-Migration Checklist

Before migrating to AWS, ensure:

- ✅ Website working perfectly on GitHub Pages
- ✅ Custom domain (br27.in) configured and tested
- ✅ SSL certificate working on GitHub Pages
- ✅ All functionality tested and verified
- ✅ AWS account created and verified
- ✅ Billing alerts configured in AWS
- ✅ IAM user created with appropriate permissions
- ✅ Backup of current site taken

---

## Option 1: AWS Amplify (Recommended) 🌟

**Best for**: Easy deployment, automatic CI/CD, minimal management
**Cost**: $0.15/month (with free tier) or ~$1-3/month after
**Difficulty**: ⭐ Easy
**Time to Deploy**: 15-20 minutes

### Why Amplify?

- ✅ Automatic deployments from GitHub
- ✅ Built-in SSL certificates
- ✅ Global CDN included
- ✅ Easy custom domain setup
- ✅ Preview deployments for branches
- ✅ Free tier: 1000 build minutes/month, 15GB served/month
- ✅ No server management

### Step-by-Step Deployment

#### 1. Access AWS Amplify Console

```bash
# Open in browser
https://console.aws.amazon.com/amplify/
```

Or using AWS CLI:
```bash
# Install AWS CLI if not already installed
brew install awscli  # macOS
# or
sudo apt install awscli  # Linux

# Configure AWS credentials
aws configure
# Enter: Access Key ID, Secret Access Key, Region (us-east-1), Output (json)
```

#### 2. Create New Amplify App

1. Click **"New app"** → **"Host web app"**
2. Choose **GitHub** as source
3. Click **"Connect to GitHub"**
4. Authorize AWS Amplify
5. Select repository: `pawoPawan/br27`
6. Select branch: `main`

#### 3. Configure Build Settings

Amplify will auto-detect it's a static site. Verify settings:

```yaml
version: 1
frontend:
  phases:
    build:
      commands: []
  artifacts:
    baseDirectory: /
    files:
      - '**/*'
  cache:
    paths: []
```

Click **Next** → **Save and deploy**

#### 4. Wait for Deployment

- Initial deployment: 2-5 minutes
- You'll get a URL like: `https://main.xxxxx.amplifyapp.com`
- Test this URL thoroughly

#### 5. Add Custom Domain (br27.in)

1. In Amplify console, click **"Domain management"**
2. Click **"Add domain"**
3. Enter: `br27.in`
4. Select both:
   - `br27.in` (apex)
   - `www.br27.in` (subdomain)
5. Click **"Configure domain"**

#### 6. Update DNS Records

Amplify will show you the required DNS records:

**Delete old GitHub Pages records first!**

Add new Amplify records:
```
Type: A
Name: @
Value: [Amplify will provide - usually CloudFront IP]

Type: CNAME
Name: www
Value: [Amplify subdomain].cloudfront.net
```

**Or use Amplify-managed DNS:**
If your domain is with Route 53:
- Amplify can automatically configure everything
- Just click "Use Route 53"

#### 7. Verify SSL Certificate

- Amplify automatically provisions SSL via AWS Certificate Manager
- Wait 5-15 minutes for certificate validation
- Status will change to "Available" when ready

#### 8. Enable Auto-Deploy

Already enabled! Every push to `main` branch automatically deploys.

Test it:
```bash
# Make a small change
echo "<!-- Test auto-deploy -->" >> index.html
git add index.html
git commit -m "Test: Amplify auto-deploy"
git push

# Check Amplify console - new build should start automatically
```

### Amplify Cost Breakdown

**Free Tier (12 months):**
- 1000 build minutes/month
- 15 GB served/month
- 5 GB stored

**After Free Tier:**
- Build minutes: $0.01 per minute
- Data transfer: $0.15 per GB
- Storage: $0.023 per GB

**Estimated Monthly Cost for BR27:**
- Small traffic (< 1GB/month): **$0.15-0.50**
- Medium traffic (5GB/month): **$1-2**
- High traffic (20GB/month): **$3-5**

---

## Option 2: S3 + CloudFront 💰

**Best for**: Maximum cost optimization, high traffic
**Cost**: $1-5/month
**Difficulty**: ⭐⭐⭐ Medium
**Time to Deploy**: 45-60 minutes

### Why S3 + CloudFront?

- ✅ Extremely cheap at scale
- ✅ Unlimited scalability
- ✅ Global edge locations
- ✅ 99.99% uptime SLA
- ✅ Pay only for what you use
- ❌ Manual deployment process
- ❌ More complex setup

### Step-by-Step Deployment

#### 1. Create S3 Bucket

```bash
# Using AWS CLI
aws s3 mb s3://br27.in --region us-east-1

# Or via Console:
# 1. Go to S3 Console
# 2. Click "Create bucket"
# 3. Bucket name: br27.in
# 4. Region: us-east-1 (required for CloudFront)
# 5. Uncheck "Block all public access"
# 6. Create bucket
```

#### 2. Enable Static Website Hosting

```bash
# Using AWS CLI
aws s3 website s3://br27.in --index-document index.html --error-document index.html

# Or via Console:
# 1. Select bucket → Properties
# 2. Scroll to "Static website hosting"
# 3. Enable
# 4. Index document: index.html
# 5. Error document: index.html
# 6. Save
```

#### 3. Configure Bucket Policy

Create file `bucket-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::br27.in/*"
    }
  ]
}
```

Apply policy:
```bash
aws s3api put-bucket-policy --bucket br27.in --policy file://bucket-policy.json
```

#### 4. Upload Website Files

```bash
# Sync all files (excluding dev files)
aws s3 sync . s3://br27.in \
  --exclude ".git/*" \
  --exclude ".gitignore" \
  --exclude "*.sh" \
  --exclude "*.md" \
  --exclude ".server.*" \
  --exclude "overview.txt" \
  --cache-control "public, max-age=31536000" \
  --metadata-directive REPLACE

# Update HTML files with shorter cache (they change more often)
aws s3 sync . s3://br27.in \
  --exclude "*" \
  --include "*.html" \
  --cache-control "public, max-age=3600" \
  --metadata-directive REPLACE
```

#### 5. Test S3 Website Endpoint

```bash
# Get website endpoint
aws s3api get-bucket-website --bucket br27.in

# Test in browser
# http://br27.in.s3-website-us-east-1.amazonaws.com
```

#### 6. Create CloudFront Distribution

```bash
# Using AWS Console (easier):
# 1. Go to CloudFront Console
# 2. Click "Create distribution"
# 3. Origin domain: br27.in.s3-website-us-east-1.amazonaws.com
#    (Use the S3 website endpoint, NOT the bucket directly)
# 4. Origin protocol: HTTP only
# 5. Viewer protocol: Redirect HTTP to HTTPS
# 6. Alternate domain names (CNAMEs): br27.in, www.br27.in
# 7. SSL certificate: Request certificate
# 8. Default root object: index.html
# 9. Create distribution
```

#### 7. Request SSL Certificate

```bash
# Must be in us-east-1 for CloudFront!
aws acm request-certificate \
  --domain-name br27.in \
  --subject-alternative-names www.br27.in \
  --validation-method DNS \
  --region us-east-1

# You'll receive certificate ARN
# Go to ACM console to see DNS validation records
# Add those CNAME records to your domain registrar
# Wait for validation (5-30 minutes)
```

#### 8. Update DNS to Point to CloudFront

```
Type: A (Alias if using Route 53)
Name: @
Value: [CloudFront distribution domain name]

Type: CNAME
Name: www
Value: [CloudFront distribution domain name]
```

If using Route 53:
- Create Alias records pointing to CloudFront
- Costs $0.50/month for hosted zone

#### 9. Create CloudFront Invalidation (for updates)

Every time you update the site:
```bash
# Upload changes
aws s3 sync . s3://br27.in --exclude ".git/*" --exclude "*.sh"

# Invalidate CloudFront cache
aws cloudfront create-invalidation \
  --distribution-id [YOUR_DISTRIBUTION_ID] \
  --paths "/*"

# Or specific files only
aws cloudfront create-invalidation \
  --distribution-id [YOUR_DISTRIBUTION_ID] \
  --paths "/index.html" "/styles.css" "/script.js"
```

#### 10. Automate Deployment (Optional)

Create `deploy-aws.sh`:

```bash
#!/bin/bash
# Deploy to AWS S3 + CloudFront

BUCKET="br27.in"
DISTRIBUTION_ID="YOUR_DISTRIBUTION_ID"

echo "Uploading to S3..."
aws s3 sync . s3://$BUCKET \
  --exclude ".git/*" \
  --exclude "*.sh" \
  --exclude "*.md" \
  --exclude ".server.*" \
  --delete

echo "Creating CloudFront invalidation..."
aws cloudfront create-invalidation \
  --distribution-id $DISTRIBUTION_ID \
  --paths "/*"

echo "Deployment complete!"
```

### S3 + CloudFront Cost Breakdown

**S3 Storage:**
- First 50 TB: $0.023 per GB
- BR27 (~5MB): **$0.12/month**

**S3 Requests:**
- GET: $0.0004 per 1000 requests
- 10,000 views: **$0.004/month**

**CloudFront Data Transfer:**
- First 10 TB: $0.085 per GB
- 5GB/month: **$0.42/month**
- 20GB/month: **$1.70/month**

**CloudFront Requests:**
- $0.0075 per 10,000 requests
- 10,000 views: **$0.08/month**

**Total Estimated Cost:**
- Low traffic: **$0.60-1.00/month**
- Medium traffic (5GB): **$1.50-2.00/month**
- High traffic (20GB): **$3-5/month**

---

## Option 3: EC2 + Nginx 🖥️

**Best for**: Need server control, plan to add backend later
**Cost**: $5-15/month
**Difficulty**: ⭐⭐⭐⭐ Advanced
**Time to Deploy**: 60-90 minutes

### Why EC2?

- ✅ Full server control
- ✅ Can add backend/APIs later
- ✅ Can run custom scripts
- ✅ SSH access
- ❌ More expensive
- ❌ Requires server management
- ❌ Manual security updates

### Step-by-Step Deployment

#### 1. Launch EC2 Instance

```bash
# Using AWS Console:
# 1. Go to EC2 Console
# 2. Click "Launch instance"
# 3. Name: BR27-Web-Server
# 4. AMI: Ubuntu Server 22.04 LTS
# 5. Instance type: t2.micro (free tier) or t3.micro
# 6. Create new key pair: br27-key.pem (download and save!)
# 7. Security group:
#    - Allow SSH (22) from your IP
#    - Allow HTTP (80) from anywhere
#    - Allow HTTPS (443) from anywhere
# 8. Storage: 8 GB (default)
# 9. Launch instance
```

#### 2. Connect to Instance

```bash
# Set key permissions
chmod 400 br27-key.pem

# Connect via SSH
ssh -i br27-key.pem ubuntu@[EC2-PUBLIC-IP]
```

#### 3. Install Nginx

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install nginx
sudo apt install nginx -y

# Start nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx

# Test: Visit http://[EC2-PUBLIC-IP] in browser
# Should see Nginx welcome page
```

#### 4. Upload Website Files

From your local machine:
```bash
# Create directory on server
ssh -i br27-key.pem ubuntu@[EC2-PUBLIC-IP] "sudo mkdir -p /var/www/br27"

# Upload files
scp -i br27-key.pem -r /Users/pawkumar/Documents/pawan/br27/* \
  ubuntu@[EC2-PUBLIC-IP]:/tmp/br27/

# Move files to web root
ssh -i br27-key.pem ubuntu@[EC2-PUBLIC-IP] \
  "sudo mv /tmp/br27/* /var/www/br27/ && sudo chown -R www-data:www-data /var/www/br27"
```

#### 5. Configure Nginx

```bash
# Create nginx config
sudo nano /etc/nginx/sites-available/br27.in
```

Add this configuration:

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name br27.in www.br27.in;

    root /var/www/br27;
    index index.html;

    # Gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml text/javascript;

    location / {
        try_files $uri $uri/ =404;
    }

    # Cache static assets
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|svg|woff|woff2|ttf|eot)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/br27.in /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

#### 6. Install SSL Certificate

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d br27.in -d www.br27.in

# Follow prompts:
# - Enter email: pkrtds03@gmail.com
# - Agree to terms: Yes
# - Redirect HTTP to HTTPS: Yes (recommended)

# Test auto-renewal
sudo certbot renew --dry-run
```

#### 7. Allocate Elastic IP (Optional but Recommended)

```bash
# In EC2 Console:
# 1. Elastic IPs → Allocate Elastic IP address
# 2. Select the new IP → Actions → Associate Elastic IP address
# 3. Select your BR27 instance
# 4. Associate

# This gives you a permanent IP that won't change if instance restarts
```

#### 8. Update DNS Records

```
Type: A
Name: @
Value: [EC2 Elastic IP]

Type: A
Name: www
Value: [EC2 Elastic IP]
```

#### 9. Set Up Automatic Updates

```bash
# Install unattended-upgrades
sudo apt install unattended-upgrades -y

# Enable automatic security updates
sudo dpkg-reconfigure -plow unattended-upgrades

# Create update script
cat > ~/update-br27.sh << 'EOF'
#!/bin/bash
cd /var/www/br27
sudo chown -R www-data:www-data .
sudo systemctl reload nginx
echo "BR27 website updated: $(date)"
EOF

chmod +x ~/update-br27.sh
```

#### 10. Future Deployment Process

To update the site:
```bash
# From local machine
scp -i br27-key.pem -r /Users/pawkumar/Documents/pawan/br27/* \
  ubuntu@[EC2-IP]:/tmp/br27/

ssh -i br27-key.pem ubuntu@[EC2-IP] \
  "sudo rsync -av --delete /tmp/br27/ /var/www/br27/ && \
   sudo chown -R www-data:www-data /var/www/br27 && \
   sudo systemctl reload nginx"
```

### EC2 Cost Breakdown

**Instance:**
- t2.micro: $0.0116/hour = **$8.35/month**
- t3.micro: $0.0104/hour = **$7.49/month**

**Storage (EBS):**
- 8 GB gp3: **$0.80/month**

**Data Transfer:**
- Out to internet: $0.09/GB after 100GB/month
- First 100GB: **Free**
- 5GB/month: **$0.00**
- 150GB/month: **$4.50**

**Elastic IP:**
- Associated: **Free**
- Unassociated: $0.005/hour

**Total Monthly Cost:**
- t2.micro: **$9-10/month**
- t3.micro: **$8-9/month**
- With high traffic: **$12-15/month**

---

## DNS Migration

### Complete DNS Setup for Each Option

#### For AWS Amplify:
```
Type: A
Name: @
Value: [Provided by Amplify]

Type: CNAME  
Name: www
Value: [your-app].amplifyapp.com
```

#### For S3 + CloudFront (with Route 53):
```
Type: A (Alias)
Name: @
Target: [distribution-id].cloudfront.net

Type: A (Alias)
Name: www
Target: [distribution-id].cloudfront.net
```

#### For S3 + CloudFront (without Route 53):
```
Type: A
Name: @
Value: [CloudFront IP from documentation]

Type: CNAME
Name: www
Value: [distribution-id].cloudfront.net
```

#### For EC2:
```
Type: A
Name: @
Value: [Elastic IP]

Type: A
Name: www
Value: [Elastic IP]
```

### DNS Propagation Timeline

- **Minimum**: 5-15 minutes
- **Typical**: 1-4 hours
- **Maximum**: 24-48 hours
- **Check status**: `dig br27.in` or [whatsmydns.net](https://whatsmydns.net)

---

## Post-Migration Testing

### Testing Checklist

```bash
# 1. DNS resolution
dig br27.in
dig www.br27.in

# 2. HTTP to HTTPS redirect
curl -I http://br27.in
# Should return 301/302 redirect to https://

# 3. HTTPS working
curl -I https://br27.in
# Should return 200 OK

# 4. SSL certificate valid
curl https://br27.in
# Should not show certificate errors

# 5. Both apex and www work
curl -I https://br27.in
curl -I https://www.br27.in

# 6. Check SSL certificate details
openssl s_client -connect br27.in:443 -servername br27.in
```

### Browser Testing

- ✅ Visit https://br27.in
- ✅ Visit https://www.br27.in
- ✅ Check all pages load
- ✅ Test all forms and buttons
- ✅ Check console for errors
- ✅ Test on mobile devices
- ✅ Check loading speed

### Performance Testing

```bash
# PageSpeed Insights
https://pagespeed.web.dev/analysis?url=https://br27.in

# GTmetrix
https://gtmetrix.com/

# WebPageTest
https://www.webpagetest.org/
```

---

## Cost Optimization

### General Tips

1. **Enable Compression**: Gzip/Brotli compression
2. **Use CDN**: CloudFront or Amplify CDN
3. **Optimize Images**: Use WebP format
4. **Minify Assets**: Minify CSS/JS
5. **Cache Headers**: Set appropriate cache times
6. **Monitor Usage**: Set up AWS billing alerts

### AWS Cost Monitoring

```bash
# Set billing alert
# 1. Go to CloudWatch
# 2. Create alarm
# 3. Metric: EstimatedCharges
# 4. Threshold: $5
# 5. Notification: Your email

# Check current costs
aws ce get-cost-and-usage \
  --time-period Start=2025-11-01,End=2025-11-30 \
  --granularity MONTHLY \
  --metrics "BlendedCost"
```

### Comparison Table

| Feature | GitHub Pages | Amplify | S3+CloudFront | EC2 |
|---------|-------------|---------|---------------|-----|
| **Cost** | FREE | $0.15-3 | $1-5 | $8-15 |
| **Setup Time** | 10 min | 20 min | 60 min | 90 min |
| **Auto Deploy** | ✅ | ✅ | ❌ | ❌ |
| **SSL** | ✅ Auto | ✅ Auto | ✅ Manual | ✅ Auto |
| **Scalability** | Medium | High | Very High | Medium |
| **Control** | Low | Low | Medium | High |
| **Backend Support** | ❌ | Limited | ❌ | ✅ |

---

## Monitoring & Maintenance

### AWS Amplify Monitoring

```bash
# Check deployment status
aws amplify list-apps

# View builds
aws amplify list-jobs --app-id [APP_ID] --branch-name main

# Check metrics in console
# - Number of requests
# - Data served
# - Build minutes used
```

### S3 + CloudFront Monitoring

```bash
# CloudWatch metrics
# 1. Go to CloudWatch Console
# 2. Create dashboard for:
#    - CloudFront: Requests, BytesDownloaded
#    - S3: NumberOfObjects, BucketSizeBytes

# Set up alarms for:
# - High request rate (DDoS detection)
# - High data transfer (cost alert)
# - 4xx/5xx errors
```

### EC2 Monitoring

```bash
# Install CloudWatch agent
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
sudo dpkg -i amazon-cloudwatch-agent.deb

# Basic monitoring (free)
# - CPU utilization
# - Disk reads/writes
# - Network in/out

# Set up alerts for:
# - High CPU (>80%)
# - High memory (>90%)
# - Disk space (>80%)
# - Failed health checks
```

---

## Migration Timeline

### Recommended Phased Approach

**Week 1: Preparation**
- ✅ Test website thoroughly on GitHub Pages
- ✅ Set up AWS account
- ✅ Configure billing alerts
- ✅ Choose migration option

**Week 2: AWS Setup**
- Deploy to AWS (test environment)
- Use subdomain like `test.br27.in`
- Test all functionality
- Compare performance

**Week 3: DNS Migration**
- Lower TTL on DNS records (to 300 seconds)
- Wait 48 hours for TTL to propagate
- Update DNS to point to AWS
- Monitor closely

**Week 4: Optimization**
- Monitor costs and performance
- Optimize as needed
- Keep GitHub Pages as backup
- Document process

---

## Rollback Plan

If something goes wrong:

1. **Immediate Rollback** (5 minutes)
   ```bash
   # Point DNS back to GitHub Pages
   # A records: 185.199.108.153 (and other 3)
   # CNAME: pawopawan.github.io
   ```

2. **Investigate Issue**
   - Check AWS console logs
   - Test AWS deployment directly
   - Identify problem

3. **Fix and Retry**
   - Fix issue in AWS
   - Test thoroughly
   - Migrate again when ready

---

## Support & Resources

### AWS Documentation
- [AWS Amplify](https://docs.aws.amazon.com/amplify/)
- [S3 Static Hosting](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)
- [CloudFront](https://docs.aws.amazon.com/cloudfront/)
- [EC2](https://docs.aws.amazon.com/ec2/)

### Cost Calculators
- [AWS Pricing Calculator](https://calculator.aws/)
- [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/)
- [S3 Pricing](https://aws.amazon.com/s3/pricing/)

### Monitoring Tools
- AWS CloudWatch
- AWS Cost Explorer
- AWS Trusted Advisor

---

## Final Recommendation

**For BR27, we recommend: AWS Amplify**

**Reasons:**
1. ✅ Easy setup and management
2. ✅ Auto-deploy from GitHub
3. ✅ Very affordable ($0.15-3/month)
4. ✅ SSL and CDN included
5. ✅ No server management
6. ✅ Can upgrade to other options later

**When to consider alternatives:**
- **S3 + CloudFront**: If traffic grows significantly (>100GB/month)
- **EC2**: If you need to add backend APIs, databases, or server-side processing

---

**Questions or Issues?**
- Email: pkrtds03@gmail.com
- GitHub: [https://github.com/pawoPawan/br27](https://github.com/pawoPawan/br27)

---

*Last Updated: Ready for AWS migration*
*Document Version: 1.0*

