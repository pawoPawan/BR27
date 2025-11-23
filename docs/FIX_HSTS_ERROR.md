# Fix HSTS Error for www.br27.in

> **Error:** "You cannot visit www.br27.in right now because the website uses HSTS"

---

## 🔴 The Error Message

```
www.br27.in normally uses encryption to protect your information.
When Chrome tried to connect to www.br27.in this time, the website
sent back unusual and incorrect credentials.

You cannot visit www.br27.in right now because the website uses HSTS.
Network errors and attacks are usually temporary, so this page will
probably work later.
```

---

## 🎯 What This Means

**HSTS = HTTP Strict Transport Security**

1. Chrome **remembers** www.br27.in requires HTTPS (secure connection)
2. www.br27.in **doesn't have valid SSL certificate** yet
3. Chrome **refuses to connect** (protecting you from potential attacks)
4. This is **GOOD** - Chrome is keeping you safe!

**Root cause:** SSL certificate not provisioned for www subdomain yet.

---

## ✅ COMPLETE FIX (2 Parts)

### **Part 1: Fix SSL Certificate on GitHub (PRIMARY FIX)**

This is the **permanent solution** - get GitHub to provision SSL for www.br27.in:

#### Step 1: Go to GitHub Pages Settings
```
https://github.com/pawoPawan/BR27/settings/pages
```

#### Step 2: Remove Custom Domain
1. Find "Custom domain" section
2. Delete `br27.in` from the text box
3. Click **"Save"**
4. **Wait 30 seconds** (important!)

#### Step 3: Re-add Custom Domain
1. Type `br27.in` back in the box
2. Click **"Save"**
3. Wait for DNS check ✅

#### Step 4: Wait for SSL Provisioning
- ⏰ **Wait 10-15 minutes**
- GitHub is requesting SSL certificate for BOTH:
  - br27.in ✅
  - www.br27.in ⏳ (being created!)

#### Step 5: Enable HTTPS Enforcement
After 15 minutes:
1. Refresh GitHub Pages settings page
2. Check "Enforce HTTPS" box
3. Click "Save"

---

### **Part 2: Clear Chrome's HSTS Cache (IMMEDIATE WORKAROUND)**

While waiting for SSL certificate, clear Chrome's memory of HSTS:

#### Step 1: Open Chrome HSTS Settings
In Chrome address bar, type:
```
chrome://net-internals/#hsts
```
Press Enter.

#### Step 2: Delete Domain Policies

Scroll down to **"Delete domain security policies"** section.

**Delete apex domain:**
1. In the "Domain" field, type: `br27.in`
2. Click **"Delete"** button
3. Should see: "Deleted HSTS for br27.in"

**Delete www subdomain:**
1. In the "Domain" field, type: `www.br27.in`
2. Click **"Delete"** button
3. Should see: "Deleted HSTS for www.br27.in"

#### Step 3: Close and Reopen Chrome
1. **Close all Chrome windows** completely
2. **Reopen Chrome**
3. Try accessing `https://www.br27.in` again

---

## 🧪 Test After Both Parts

**After completing Part 1 (SSL fix) + Part 2 (HSTS clear):**

### Test 1: In Chrome (HSTS cleared)
```
https://www.br27.in  ← Should work after 20 minutes!
```

### Test 2: In Incognito Mode (Bypasses HSTS cache)
```
Open Chrome → New Incognito Window → https://www.br27.in
```

### Test 3: In Different Browser
```
Firefox, Safari, or Edge → https://www.br27.in
```

If it works in incognito/other browsers but not regular Chrome:
→ You need to clear HSTS cache (Part 2 above)

---

## ⏰ Timeline

| Action | Time |
|--------|------|
| Remove + re-add domain | 2 min |
| Wait for SSL | 15 min |
| Enable HTTPS | 1 min |
| Clear HSTS cache | 2 min |
| **TOTAL** | **~20 min** |

**After 20 minutes:** All browsers should work!

---

## 🔄 Alternative Access Methods (While Fixing)

**While waiting for SSL certificate:**

### Method 1: Use Apex Domain
```
https://br27.in  ← This works right now!
```
Share this URL instead of www.br27.in for now.

### Method 2: Use Incognito/Private Browsing
```
Chrome → New Incognito Window
Firefox → New Private Window
Safari → New Private Window
```
Then visit: `https://www.br27.in`

Incognito bypasses HSTS cache, but will still show SSL error until GitHub provisions certificate.

### Method 3: Use Different Browser
If error persists in Chrome, try:
- Firefox
- Safari
- Edge
- Brave

---

## 🆘 Troubleshooting

### Error Still Shows After 30 Minutes?

#### Check 1: Verify SSL Certificate is Ready
```bash
# In terminal, check if certificate covers www:
curl -I https://www.br27.in

# Should return: HTTP/2 200
# If error: SSL not ready yet, wait longer
```

#### Check 2: Verify HSTS is Cleared in Chrome
1. Go to: `chrome://net-internals/#hsts`
2. Scroll to "Query HSTS/PKP domain"
3. Type: `www.br27.in`
4. Click "Query"
5. Should say: "Not found" (good!)

If it shows "Found", delete it again (Part 2 above).

#### Check 3: Clear ALL Browser Data
If HSTS delete didn't work:

1. Chrome Settings (⋮ menu)
2. Privacy and security
3. Clear browsing data
4. Time range: "All time"
5. Check: "Cookies and other site data"
6. Click "Clear data"
7. Restart Chrome

⚠️ **Warning:** This logs you out of all websites!

### Error in ALL Browsers?

If error shows in Chrome, Firefox, Safari, Edge:
- SSL certificate is NOT ready yet
- Wait longer (up to 30 minutes total)
- Verify GitHub Pages shows "Enforce HTTPS" enabled
- Check GitHub status: https://www.githubstatus.com

---

## 📱 Mobile Devices

### Same HSTS Error on Phone?

**Android Chrome:**
1. Chrome → Settings → Privacy → Clear browsing data
2. Select "All time"
3. Check "Cookies and site data"
4. Clear data
5. Restart Chrome

**iOS Safari:**
1. Settings → Safari → Clear History and Website Data
2. Confirm
3. Reopen Safari

**Alternative:** Use apex domain `br27.in` on mobile for now.

---

## 🎯 Why This Happened

### Timeline of Events:

1. **Initial setup:** GitHub Pages enabled for br27.in
2. **SSL for apex:** Certificate issued for `br27.in` ✅
3. **HSTS enabled:** GitHub automatically enabled HSTS
4. **Browser visited:** Chrome accessed `www.br27.in` (redirected from br27.in)
5. **HSTS cached:** Chrome remembered: "www.br27.in MUST use HTTPS"
6. **SSL missing:** Certificate for `www.br27.in` not provisioned yet ❌
7. **Chrome blocks:** HSTS prevents insecure connection (protecting you!)

### This is Actually GOOD Security!

Chrome is **protecting you** from:
- Man-in-the-middle attacks
- Downgrade attacks
- Unencrypted connections

Once SSL is provisioned, everything works perfectly!

---

## ✅ Success Indicators

You'll know it's fixed when:

### In Chrome (after clearing HSTS)
```
✅ No HSTS error message
✅ Green padlock 🔒 in address bar
✅ URL shows: https://www.br27.in
✅ Website loads normally
```

### In GitHub Pages Settings
```
✅ Custom domain: br27.in
✅ DNS check: ✅ Successful
✅ Enforce HTTPS: ☑ Enabled
✅ Your site is published at: https://br27.in
```

### Certificate Check (Terminal)
```bash
# Check certificate covers both domains:
echo "Q" | openssl s_client -connect www.br27.in:443 -servername www.br27.in 2>/dev/null | openssl x509 -noout -text | grep -A1 "Subject Alternative Name"

# Should show:
# DNS:br27.in, DNS:www.br27.in
```

---

## 🚀 Final Result

**Before Fix:**
```
❌ www.br27.in → HSTS Error
✅ br27.in     → Working
```

**After Fix (20 minutes):**
```
✅ www.br27.in → Working perfectly! 🔒
✅ br27.in     → Working perfectly! 🔒
```

**All these URLs work:**
```
✅ https://br27.in
✅ https://www.br27.in
✅ http://br27.in        (redirects to HTTPS)
✅ http://www.br27.in    (redirects to HTTPS)
✅ br27.in               (browser adds HTTPS)
✅ www.br27.in           (browser adds HTTPS)
```

---

## 📋 Quick Action Checklist

**Do these in order:**

- [ ] Go to GitHub Pages settings
- [ ] Remove `br27.in` from custom domain
- [ ] Wait 30 seconds
- [ ] Re-add `br27.in` to custom domain
- [ ] Wait 15 minutes for SSL provisioning
- [ ] Enable "Enforce HTTPS" checkbox
- [ ] Open `chrome://net-internals/#hsts`
- [ ] Delete HSTS for `br27.in`
- [ ] Delete HSTS for `www.br27.in`
- [ ] Close and reopen Chrome
- [ ] Test `https://www.br27.in`
- [ ] ✅ Working!

---

## 💡 Pro Tips

1. **Use Incognito for testing** - bypasses all caches
2. **Clear HSTS cache first** - saves frustration while waiting
3. **Don't panic** - HSTS errors look scary but are actually good security
4. **Use br27.in temporarily** - works right now while www is being fixed
5. **Wait the full time** - SSL provisioning can't be rushed
6. **Check other browsers** - helps diagnose if it's HSTS cache issue

---

## 📚 Related Documentation

- **`FIX_WWW_SSL_ERROR.md`** - Complete SSL certificate fix guide
- **`QUICK_SSL_FIX.md`** - Quick 3-step SSL fix
- **`QUICK_DOMAIN_REFERENCE.md`** - Domain access reference

---

## 🔗 Useful Links

**Chrome HSTS Management:**
```
chrome://net-internals/#hsts
```

**GitHub Pages Settings:**
```
https://github.com/pawoPawan/BR27/settings/pages
```

**Check SSL Certificate:**
```
https://www.ssllabs.com/ssltest/analyze.html?d=www.br27.in
```

**GitHub Status:**
```
https://www.githubstatus.com
```

---

*Last Updated: November 23, 2025*  
*Error: HSTS + NET::ERR_CERT_COMMON_NAME_INVALID*  
*Solution: Provision SSL certificate + Clear HSTS cache*

