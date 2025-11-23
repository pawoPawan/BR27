# Fix "Your connection is not private" Error for www.br27.in

> **Error:** NET::ERR_CERT_COMMON_NAME_INVALID when accessing https://www.br27.in

---

## 🔴 Problem

- ✅ `https://br27.in` works perfectly
- ❌ `https://www.br27.in` shows SSL certificate error
- **Cause:** GitHub Pages hasn't provisioned SSL certificate for www subdomain

---

## ✅ IMMEDIATE FIX (5 minutes + 15 min wait)

### **Step 1: Access GitHub Pages Settings**

1. Open your browser
2. Go to: **https://github.com/pawoPawan/BR27/settings/pages**
3. Log in if needed

### **Step 2: Remove Custom Domain**

1. Find the **"Custom domain"** section
2. You should see: `br27.in` in the text box
3. **Select all the text** and **delete it**
4. Click the **"Save"** button
5. **WAIT 30 SECONDS** (very important - don't rush!)

**Screenshot location:**
```
GitHub → Repository Settings → Pages → Custom domain: [br27.in] ← Delete this
```

### **Step 3: Re-add Custom Domain**

1. In the **same "Custom domain"** text box (now empty)
2. Type: `br27.in` (without quotes)
3. Click **"Save"**
4. GitHub will perform a DNS check
5. Wait for **green checkmark** ✅ to appear

**You should see:**
```
✅ DNS check successful
```

### **Step 4: Wait for SSL Certificate Provisioning**

⏰ **Wait 10-15 minutes** for GitHub to:
- Provision SSL certificate for `br27.in`
- Provision SSL certificate for `www.br27.in`
- Both domains included in same certificate

**During this time:**
- Don't refresh the page repeatedly
- Don't make any more DNS changes
- Be patient - this is automatic

### **Step 5: Enable HTTPS Enforcement**

After 10-15 minutes:

1. Refresh the GitHub Pages settings page
2. Look for **"Enforce HTTPS"** checkbox
3. If it's **enabled** (you can click it): ✅ SSL is ready!
4. **Check the box** to enforce HTTPS
5. Click **"Save"**

**If "Enforce HTTPS" is still disabled:**
- Message shows: "Unavailable for your site because..."
- Wait another 10 minutes
- Refresh the page
- Try again

### **Step 6: Test Your Website**

After enabling "Enforce HTTPS", test all URLs:

```bash
# Test 1: Apex domain
https://br27.in          ← Should work ✅

# Test 2: WWW subdomain
https://www.br27.in      ← Should work ✅ (was broken before)

# Test 3: HTTP redirects
http://br27.in           ← Redirects to HTTPS ✅
http://www.br27.in       ← Redirects to HTTPS ✅
```

Open each URL in your browser - **no more SSL errors!** 🎉

---

## 🧪 Verify SSL Certificate

### Check Certificate Details

1. Visit: `https://br27.in` in Chrome
2. Click the **padlock icon** 🔒 in address bar
3. Click **"Certificate"**
4. Look for **"Subject Alternative Name"**
5. Should show:
   ```
   DNS Name: br27.in
   DNS Name: www.br27.in
   ```

Both domains should be listed! ✅

### Command Line Check (Optional)

```bash
# Check what domains the certificate covers
echo "Q" | openssl s_client -connect br27.in:443 -servername br27.in 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"

# Should show both br27.in and www.br27.in
```

---

## ⏰ Timeline

| Step | Time Required |
|------|---------------|
| Remove + re-add domain | 2 minutes |
| Wait for SSL provisioning | 10-15 minutes |
| Enable HTTPS enforcement | 1 minute |
| **TOTAL** | **~15-20 minutes** |

---

## 🆘 If It Still Doesn't Work

### After 30 Minutes

If `www.br27.in` still shows SSL error after 30 minutes:

#### Try 1: Repeat the Process
1. Remove `br27.in` from custom domain
2. Wait **2 minutes** (longer this time)
3. Re-add `br27.in`
4. Wait **20 minutes**
5. Enable HTTPS

#### Try 2: Check DNS
```bash
# Verify DNS is correct
dig www.br27.in +short

# Should show:
# br27.in.
# 185.199.108.153
# 185.199.109.153
# 185.199.110.153
# 185.199.111.153
```

If DNS is wrong, fix in GoDaddy:
- Go to GoDaddy DNS Management
- Verify CNAME: `www` → `br27.in`
- Save and wait 10 minutes

#### Try 3: Check GitHub Status
```
https://www.githubstatus.com
```

If GitHub Pages has issues, wait for them to resolve it.

#### Try 4: Use Apex Domain Only

Temporary workaround while waiting:
- Share `https://br27.in` (without www)
- Tell people to use `br27.in` instead of `www.br27.in`
- Both will work once SSL is provisioned

---

## 🎯 Why This Happens

GitHub Pages provisions SSL certificates through Let's Encrypt:

1. **Initial Setup:** Certificate for apex domain (`br27.in`) ✅
2. **Later:** Certificate needs to include www subdomain
3. **Refresh Needed:** Remove + re-add triggers new certificate request
4. **Automatic:** GitHub requests certificate for both domains
5. **Complete:** Both domains covered by same certificate

**This is normal!** Happens frequently with GitHub Pages custom domains.

---

## ✅ Success Indicators

You'll know it's fixed when:

1. ✅ No SSL warning when visiting `https://www.br27.in`
2. ✅ Green padlock 🔒 appears in browser
3. ✅ "Enforce HTTPS" checkbox is enabled in GitHub settings
4. ✅ Both `br27.in` and `www.br27.in` show same content
5. ✅ HTTP URLs auto-redirect to HTTPS

---

## 📞 Still Need Help?

### Check These Resources

1. **GitHub Pages Documentation**
   ```
   https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages
   ```

2. **SSL Certificate Status**
   ```
   https://www.ssllabs.com/ssltest/analyze.html?d=br27.in
   ```

3. **DNS Propagation**
   ```
   https://dnschecker.org/?domain=www.br27.in
   ```

### GitHub Pages Support

If nothing works after 24 hours:
1. Check GitHub Pages status page
2. Verify repository is public
3. Verify main branch has content
4. Verify CNAME file exists with `br27.in`

---

## 📋 Quick Checklist

Before asking for help, verify:

- [ ] DNS A records point to GitHub IPs
- [ ] DNS CNAME for www points to br27.in
- [ ] Custom domain in GitHub settings shows `br27.in`
- [ ] DNS check shows green checkmark in GitHub
- [ ] Waited at least 30 minutes after re-adding domain
- [ ] Repository is public (not private)
- [ ] Main branch is selected as source
- [ ] CNAME file exists in repository root
- [ ] GitHub Pages shows "Your site is published at..."

---

## 🎉 Expected Final Result

After following these steps:

```
✅ https://br27.in          → Works perfectly
✅ https://www.br27.in      → Works perfectly (FIXED!)
✅ http://br27.in           → Redirects to HTTPS
✅ http://www.br27.in       → Redirects to HTTPS
```

**All SSL warnings gone!** 🔒🎊

---

## 💡 Pro Tips

1. **Bookmark the GitHub Pages settings page** for quick access
2. **Always wait 30 seconds** between removing and re-adding domain
3. **Don't remove domain multiple times** - wait for SSL to provision
4. **Use incognito/private browsing** when testing to avoid cache
5. **Clear browser cache** if you still see errors after fix

---

*Last Updated: November 23, 2025*  
*Issue: NET::ERR_CERT_COMMON_NAME_INVALID*  
*Solution: Remove and re-add custom domain to trigger SSL refresh*

