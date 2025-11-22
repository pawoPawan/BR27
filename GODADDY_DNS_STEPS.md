# 🌐 GoDaddy DNS Setup for br27.in → GitHub Pages

## ✅ Your Domain: br27.in (Registered with GoDaddy)

Follow these exact steps to point your domain to GitHub Pages:

---

## 📋 Step 1: Log into GoDaddy

1. **Go to:** https://dnsmanagement.godaddy.com/
2. **Sign in** with your GoDaddy credentials
3. You'll see a list of your domains

---

## 📋 Step 2: Access DNS Settings for br27.in

1. Find **br27.in** in your domain list
2. Click the **DNS** button next to it (or click the domain name, then click "DNS")
3. You'll see the DNS Management page

---

## 📋 Step 3: Remove Old A Records (if any exist)

**Look for existing A records pointing to:**
- 76.223.105.230
- 13.248.243.5
- Or any other IP addresses

**To remove:**
1. Find each A record with **@** or **br27.in** in the Name field
2. Click the **pencil icon** (edit) or **trash icon** (delete)
3. Delete all old A records
4. Keep any other records (TXT, MX, etc.) - DON'T delete those!

---

## 📋 Step 4: Add GitHub Pages A Records

Click **Add** button and create these 4 A records:

### Record 1:
```
Type:     A
Name:     @
Value:    185.199.108.153
TTL:      1 Hour (or Default)
```
Click **Save**

### Record 2:
```
Type:     A
Name:     @
Value:    185.199.109.153
TTL:      1 Hour (or Default)
```
Click **Save**

### Record 3:
```
Type:     A
Name:     @
Value:    185.199.110.153
TTL:      1 Hour (or Default)
```
Click **Save**

### Record 4:
```
Type:     A
Name:     @
Value:    185.199.111.153
TTL:      1 Hour (or Default)
```
Click **Save**

---

## 📋 Step 5: Add CNAME Record for www

Look for existing CNAME record with **www**:
- If exists, click **edit** and update it
- If doesn't exist, click **Add** to create new

```
Type:     CNAME
Name:     www
Value:    pawopawan.github.io
TTL:      1 Hour (or Default)
```
Click **Save**

**Important:** 
- GoDaddy might automatically add a dot (.) at the end
- That's fine! Both `pawopawan.github.io` and `pawopawan.github.io.` work

---

## 📋 Step 6: Verify Your Changes

After saving, your DNS records should look like this:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 1 Hour |
| A | @ | 185.199.109.153 | 1 Hour |
| A | @ | 185.199.110.153 | 1 Hour |
| A | @ | 185.199.111.153 | 1 Hour |
| CNAME | www | pawopawan.github.io | 1 Hour |

**Screenshot this for reference!**

---

## ⏱️ Step 7: Wait for DNS Propagation

- **GoDaddy typically takes:** 30-60 minutes
- **Maximum time:** Up to 48 hours (rare)
- **Check progress:** https://www.whatsmydns.net/#A/br27.in

### What to expect:
- ⏰ **0-5 min:** Changes saved in GoDaddy
- ⏰ **5-30 min:** DNS starts propagating
- ⏰ **30-60 min:** Most locations worldwide updated
- ✅ **60+ min:** Fully propagated everywhere

---

## 🔍 Step 8: Verify DNS is Working

### Method 1: Online Tool
1. Go to: https://www.whatsmydns.net/#A/br27.in
2. You should see the 4 GitHub IP addresses appearing in different locations
3. Green checkmarks mean DNS is working in that location

### Method 2: Command Line
```bash
# Check A records
nslookup br27.in

# Should return:
# Name: br27.in
# Address: 185.199.108.153
# Address: 185.199.109.153
# Address: 185.199.110.153
# Address: 185.199.111.153
```

### Method 3: Test in Browser
After 30-60 minutes:
1. Open **incognito/private window** (to avoid cache)
2. Visit: http://br27.in
3. Should redirect to https://br27.in and show your website!

---

## ⚠️ Common GoDaddy Issues & Solutions

### Issue 1: "I don't see the DNS button"
**Solution:**
- Make sure you're logged into the correct GoDaddy account
- If domain is in a different account, switch accounts
- Or go to: https://account.godaddy.com/products

### Issue 2: "Domain is using custom nameservers"
**Solution:**
- Click on **Nameservers** section
- If it shows custom nameservers (not GoDaddy's)
- Change to: **"Use GoDaddy nameservers"**
- Then add the A and CNAME records

### Issue 3: "Can't delete old A records"
**Solution:**
- Make sure you're editing the right domain (br27.in)
- Some records might be locked - look for unlock option
- If stuck, contact GoDaddy support

### Issue 4: "CNAME conflicts with A record"
**Solution:**
- A records should be for **@** (apex domain)
- CNAME should be for **www** only
- Never have CNAME for @ - use A records instead

### Issue 5: "Changes not saving"
**Solution:**
- Scroll down and click final **Save** button at bottom
- Look for confirmation message
- Try different browser if issues persist

---

## 📱 GoDaddy Mobile App

If using the GoDaddy mobile app:

1. Open **GoDaddy app**
2. Tap **Domains**
3. Tap **br27.in**
4. Tap **DNS** or **Manage DNS**
5. Add the same A and CNAME records
6. Follow same steps as above

---

## 🎯 After DNS Propagates

### 1. Configure GitHub Pages Custom Domain

1. Go to: https://github.com/pawoPawan/BR27/settings/pages
2. Under **Custom domain**, enter: `br27.in`
3. Click **Save**
4. Wait for "DNS check successful" message (appears when DNS is propagated)
5. Check **"Enforce HTTPS"** (appears after DNS check passes)

### 2. Wait for HTTPS Certificate

- GitHub automatically issues SSL certificate
- Takes 10-30 minutes after DNS check succeeds
- You'll see green checkmark: "Your site is published at https://br27.in"

### 3. Test Everything

Visit these URLs (in incognito mode):
- [ ] http://br27.in → should redirect to https://br27.in ✓
- [ ] https://br27.in → should show your website ✓
- [ ] http://www.br27.in → should redirect to https://br27.in ✓
- [ ] https://www.br27.in → should redirect to https://br27.in ✓

Test features:
- [ ] Language toggle (🌐 हिंदी / English) works
- [ ] All navigation links work
- [ ] Contact form submits
- [ ] Mobile responsive
- [ ] HTTPS padlock shows 🔒

---

## 📞 GoDaddy Support

If you need help:

### Live Chat:
- https://www.godaddy.com/contact-us
- Available 24/7
- Usually fastest option

### Phone Support:
- India: 000-800-040-1843 (toll-free)
- International: Check GoDaddy website for your country

### What to Tell Them:
"I need to point my domain br27.in to GitHub Pages. Please help me add these DNS records:
- 4 A records pointing @ to GitHub Pages IPs: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- 1 CNAME record pointing www to pawopawan.github.io"

---

## ✅ Success Criteria

You'll know it's working when:

1. **In GoDaddy:** All 4 A records and 1 CNAME record visible
2. **In whatsmydns.net:** Green checkmarks showing GitHub IPs worldwide  
3. **In GitHub:** "DNS check successful" with green checkmark
4. **In Browser:** br27.in loads your website with HTTPS 🔒
5. **Language Toggle:** Switching between English/Hindi works perfectly

---

## 🎉 Expected Result

Within 1-2 hours, your website will be live at:

**🌐 https://br27.in**

Features that will work:
- ✅ Bilingual (English & Hindi)
- ✅ Modern, responsive design
- ✅ Contact form (via Formspree)
- ✅ 6 Focus Areas content
- ✅ LinkedIn & YouTube links
- ✅ HTTPS secure connection
- ✅ Fast loading (GitHub CDN)
- ✅ Mobile optimized

---

## 📊 Timeline Summary

| Step | Time |
|------|------|
| Login to GoDaddy | 1 min |
| Delete old records | 2 min |
| Add new A records | 3 min |
| Add CNAME record | 1 min |
| DNS propagation | 30-60 min |
| Set custom domain in GitHub | 2 min |
| HTTPS certificate | 10-30 min |
| **Total** | ~1-2 hours |

---

**👉 Next Action:** Log into GoDaddy at https://dnsmanagement.godaddy.com/ and follow the steps above! 🚀

Once DNS propagates, your website will be accessible worldwide at br27.in!

