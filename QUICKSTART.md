# 🚀 Quick Start Guide - Deploy to GitHub Pages

Get your BR27 website live on **br27.in** in 5 minutes!

## Option 1: Automated Deployment (Easiest) ⚡

```bash
# Run the automated deployment script
./deploy-github.sh

# Or with a custom commit message
./deploy-github.sh "Initial deployment of BR27 website"
```

The script will:
- ✅ Initialize git (if needed)
- ✅ Ask for your GitHub repository URL (if needed)
- ✅ Stage and commit all changes
- ✅ Push to GitHub
- ✅ Show your deployment URLs

---

## Option 2: Manual Deployment (Step by Step) 📝

### Step 1: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `br27` (or any name)
3. Make it **Public**
4. Don't initialize with README
5. Click **Create repository**

### Step 2: Push Your Code

```bash
cd /Users/pawkumar/Documents/pawan/br27

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: BR27 website"

# Add remote (replace with YOUR repository URL)
git remote add origin https://github.com/pawoPawan/br27.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. **Settings** → **Pages** (left sidebar)
3. Under "Source":
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**
5. Wait 2-5 minutes ⏱️

Your site will be live at: `https://pawopawan.github.io/br27/`

---

## 🌐 Configure Custom Domain (br27.in)

### Step 1: Update DNS Settings

Go to your domain registrar and add these records:

#### A Records (for br27.in):
```
Type: A,  Name: @,  Value: 185.199.108.153
Type: A,  Name: @,  Value: 185.199.109.153
Type: A,  Name: @,  Value: 185.199.110.153
Type: A,  Name: @,  Value: 185.199.111.153
```

#### CNAME Record (for www.br27.in):
```
Type: CNAME,  Name: www,  Value: pawopawan.github.io
```

### Step 2: Configure on GitHub

1. Go to repository **Settings** → **Pages**
2. Custom domain: `br27.in`
3. Click **Save**
4. Wait for DNS check ✅
5. Enable **Enforce HTTPS** 🔒

### Step 3: Wait for DNS Propagation

- Usually takes 24-48 hours
- Check status: [whatsmydns.net](https://www.whatsmydns.net/#A/br27.in)
- Once propagated: Visit `https://br27.in` 🎉

---

## 🔄 Making Updates

After initial deployment, update your site anytime:

### Using the script:
```bash
./deploy-github.sh "Added new features"
```

### Manual method:
```bash
git add .
git commit -m "Your update message"
git push
```

GitHub Pages auto-deploys within 1-5 minutes! ⚡

---

## ✅ Verification Checklist

- [ ] Code pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Site accessible at GitHub Pages URL
- [ ] CNAME file exists in repository
- [ ] DNS records configured
- [ ] Custom domain added on GitHub
- [ ] DNS propagated (24-48 hours)
- [ ] HTTPS enabled
- [ ] Site accessible at https://br27.in

---

## 📞 Need Help?

**Common Issues:**

1. **"Permission denied (publickey)"**
   - Set up SSH keys or use HTTPS URL
   - Guide: [GitHub SSH Keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

2. **"Site not updating"**
   - Check Actions tab for deployment status
   - Clear browser cache (Ctrl+Shift+R)
   - Wait 5 minutes for GitHub Pages rebuild

3. **"Custom domain not working"**
   - Verify DNS records are correct
   - Wait 24-48 hours for propagation
   - Check DNS: `dig br27.in` or use whatsmydns.net

4. **"404 Error"**
   - Ensure `index.html` is in root directory
   - Check Settings → Pages configuration

---

## 🎯 Next Steps

Once live on GitHub Pages:

1. ✅ Share your website: `https://br27.in`
2. 📊 Add Google Analytics (see DEPLOYMENT.md)
3. 🔍 Submit to Google Search Console
4. 📱 Test on mobile devices
5. ⚡ Consider AWS migration for more features

For detailed AWS migration guide, see **DEPLOYMENT.md**

---

**Congratulations! You're now live! 🚀**

*Empowering minds. Enabling progress.*

