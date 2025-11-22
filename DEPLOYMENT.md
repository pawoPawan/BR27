# BR27 Deployment Guide

This guide covers deploying BR27 to GitHub Pages and later migrating to AWS.

## 📋 Table of Contents

- [GitHub Pages Deployment](#github-pages-deployment)
- [Custom Domain Setup (br27.in)](#custom-domain-setup)
- [AWS Migration Guide](#aws-migration-guide)

---

## 🚀 GitHub Pages Deployment

### Prerequisites

- GitHub account ([pawoPawan](https://github.com/pawoPawan))
- Git installed on your machine
- Domain access for br27.in

### Step 1: Initialize Git Repository

```bash
cd /Users/pawkumar/Documents/pawan/br27

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: BR27 website - Empowering minds, enabling progress"
```

### Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named `br27` (or `br27-website`)
3. **Important**: Make it **Public** (required for GitHub Pages on free tier)
4. **Do NOT** initialize with README, .gitignore, or license (we already have these)

### Step 3: Push to GitHub

```bash
# Add remote repository (replace with your actual repo name)
git remote add origin https://github.com/pawoPawan/br27.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** → **Pages** (in the left sidebar)
3. Under "Source", select:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/ (root)`
4. Click **Save**

### Step 5: Wait for Deployment

- GitHub will automatically deploy your site
- It usually takes 1-5 minutes
- You'll see a message: "Your site is live at `https://pawopawan.github.io/br27/`"

---

## 🌐 Custom Domain Setup (br27.in)

### Step 1: Add CNAME File

✅ **Already done!** The `CNAME` file has been created with `br27.in`

### Step 2: Configure DNS Settings

Go to your domain registrar (where you bought br27.in) and add these DNS records:

#### Option A: Using Apex Domain (br27.in)

Add **A records** pointing to GitHub Pages IPs:

```
Type: A
Name: @
Value: 185.199.108.153

Type: A
Name: @
Value: 185.199.109.153

Type: A
Name: @
Value: 185.199.110.153

Type: A
Name: @
Value: 185.199.111.153
```

#### Option B: Using www subdomain (www.br27.in)

Add a **CNAME record**:

```
Type: CNAME
Name: www
Value: pawopawan.github.io
```

#### Recommended: Both configurations

Set up both A records and CNAME for maximum compatibility.

### Step 3: Configure Custom Domain on GitHub

1. Go to repository **Settings** → **Pages**
2. Under "Custom domain", enter: `br27.in`
3. Click **Save**
4. Wait for DNS check (can take 24-48 hours)
5. Once verified, enable "Enforce HTTPS" ✅

### Step 4: Verify

After DNS propagation (24-48 hours):
- Visit `https://br27.in` 
- Should see your BR27 website with SSL certificate 🔒

---

## ☁️ AWS Migration Guide

When you're ready to move to AWS, here are the recommended approaches:

### Option 1: AWS S3 + CloudFront (Static Hosting - Recommended)

**Pros**: Cheap, fast, scalable, easy
**Cost**: ~$1-5/month for small traffic

#### Steps:

1. **Create S3 Bucket**
   ```bash
   aws s3 mb s3://br27.in
   ```

2. **Configure for Static Website Hosting**
   - Enable static website hosting
   - Set index document: `index.html`
   - Set error document: `index.html` (for SPA behavior)

3. **Upload Files**
   ```bash
   aws s3 sync . s3://br27.in --exclude ".git/*" --exclude ".server.*" --exclude "setup.sh"
   ```

4. **Set up CloudFront**
   - Create CloudFront distribution
   - Origin: Your S3 bucket
   - Enable HTTPS with ACM certificate
   - Add alternate domain: `br27.in`, `www.br27.in`

5. **Update DNS**
   - Point `br27.in` to CloudFront distribution
   - Update A record to CloudFront alias

6. **Enable SSL**
   - Request certificate in AWS Certificate Manager
   - Validate domain ownership
   - Attach to CloudFront

### Option 2: AWS Amplify (Easiest)

**Pros**: Auto-deploy from GitHub, built-in CI/CD, SSL, CDN
**Cost**: ~$0.15/month (free tier available)

#### Steps:

1. Go to [AWS Amplify Console](https://console.aws.amazon.com/amplify/)
2. Click **"New app"** → **"Host web app"**
3. Connect to your GitHub repository
4. Configure build settings (use defaults for static site)
5. Add custom domain `br27.in`
6. AWS handles SSL certificates automatically
7. Auto-deploys on every push to main branch

### Option 3: EC2 with Nginx (More Control)

**Pros**: Full control, can run backend later
**Cost**: ~$5-10/month (t2.micro)

#### Quick Setup:

```bash
# Install nginx
sudo apt update
sudo apt install nginx

# Copy files to web root
sudo cp -r /path/to/br27/* /var/www/html/

# Configure nginx
sudo nano /etc/nginx/sites-available/br27.in

# Enable site
sudo ln -s /etc/nginx/sites-available/br27.in /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Set up SSL with Let's Encrypt
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d br27.in -d www.br27.in
```

### Cost Comparison

| Solution | Monthly Cost | Complexity | Auto-Deploy |
|----------|-------------|------------|-------------|
| GitHub Pages | **FREE** | Very Easy | ✅ Yes |
| AWS S3 + CloudFront | $1-5 | Medium | Manual |
| AWS Amplify | $0.15 | Easy | ✅ Yes |
| EC2 + Nginx | $5-10 | Hard | Manual |

---

## 🔄 Migration Checklist

When moving from GitHub Pages to AWS:

- [ ] Test AWS deployment with temporary URL
- [ ] Verify all pages and features work
- [ ] Update DNS records to point to AWS
- [ ] Wait for DNS propagation (24-48 hours)
- [ ] Verify HTTPS certificate works
- [ ] Test from multiple locations/devices
- [ ] Keep GitHub Pages as backup for 30 days
- [ ] Update documentation with new deployment process

---

## 🔐 Security Best Practices

### For GitHub Pages:
- ✅ Enable HTTPS (enforced)
- ✅ Use CNAME file for domain
- ✅ Keep repository public (or upgrade for private)
- ✅ Review commit history before pushing

### For AWS:
- Use IAM roles with minimal permissions
- Enable CloudFront with WAF for DDoS protection
- Use S3 bucket policies to restrict access
- Enable CloudTrail for audit logs
- Set up CloudWatch alarms for monitoring
- Regular security audits

---

## 📊 Monitoring & Analytics

### Add Google Analytics (Optional)

Add before closing `</head>` tag in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### GitHub Pages Analytics

- Use GitHub Insights tab to see traffic
- View clones and visitor statistics

---

## 🆘 Troubleshooting

### GitHub Pages Issues

**Problem**: Site not showing up
- Solution: Check Settings → Pages, ensure branch is set correctly
- Wait 5-10 minutes for deployment

**Problem**: Custom domain not working
- Solution: Verify DNS records are correct
- Check CNAME file exists in repository root
- Wait 24-48 hours for DNS propagation

**Problem**: 404 errors
- Solution: Ensure `index.html` is in root directory
- Check file names are correct (case-sensitive)

### AWS Issues

**Problem**: S3 bucket access denied
- Solution: Check bucket policy and public access settings

**Problem**: CloudFront serving old content
- Solution: Create invalidation for `/*`

**Problem**: SSL certificate issues
- Solution: Verify domain ownership in ACM
- Ensure certificate is in us-east-1 region for CloudFront

---

## 📞 Support

- **GitHub**: [https://github.com/pawoPawan/br27](https://github.com/pawoPawan/br27)
- **Email**: pkrtds03@gmail.com
- **GitHub Issues**: Report bugs and feature requests
- **AWS Support**: Available in AWS Console

---

## 🎯 Next Steps

1. ✅ Deploy to GitHub Pages
2. ✅ Configure custom domain (br27.in)
3. ⏳ Monitor traffic and performance
4. ⏳ Plan AWS migration when needed
5. ⏳ Add analytics and monitoring
6. ⏳ Consider adding blog/content sections

---

**Built with ❤️ for BR27 - Empowering minds, enabling progress**

