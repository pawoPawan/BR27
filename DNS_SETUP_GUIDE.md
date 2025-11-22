# 🌐 DNS Setup Guide for br27.in

## ⚠️ IMPORTANT: Manual Steps Required

I cannot directly access your domain registrar account to configure DNS. You need to log into your domain provider's dashboard where you purchased **br27.in**.

---

## 📋 Required DNS Records

Copy these exact values and add them to your domain's DNS settings:

### **A Records** (For apex domain: br27.in)

```
Record 1:
Type:     A
Name:     @ (or leave blank, or br27.in)
Value:    185.199.108.153
TTL:      3600 (or Auto)

Record 2:
Type:     A
Name:     @ (or leave blank, or br27.in)
Value:    185.199.109.153
TTL:      3600 (or Auto)

Record 3:
Type:     A
Name:     @ (or leave blank, or br27.in)
Value:    185.199.110.153
TTL:      3600 (or Auto)

Record 4:
Type:     A
Name:     @ (or leave blank, or br27.in)
Value:    185.199.111.153
TTL:      3600 (or Auto)
```

### **CNAME Record** (For www subdomain)

```
Type:     CNAME
Name:     www
Value:    pawopawan.github.io.
TTL:      3600 (or Auto)
```

**Note:** Make sure the CNAME value ends with a dot (.)

---

## 🔧 Step-by-Step Instructions by Provider

### **Common Providers:**

<details>
<summary><b>GoDaddy</b></summary>

1. Go to: https://dnsmanagement.godaddy.com/
2. Log in with your credentials
3. Find **br27.in** and click **DNS**
4. Scroll to **Records** section
5. Click **Add** for each record:
   - Select **A** as Type
   - Enter **@** in Name
   - Enter the IP address in Value
   - Repeat for all 4 A records
6. Add CNAME record:
   - Select **CNAME** as Type
   - Enter **www** in Name
   - Enter **pawopawan.github.io** in Value
7. Click **Save**
8. Wait 10-60 minutes for propagation

</details>

<details>
<summary><b>Namecheap</b></summary>

1. Go to: https://ap.www.namecheap.com/
2. Click **Domain List**
3. Find **br27.in** and click **Manage**
4. Go to **Advanced DNS** tab
5. Under **Host Records**, click **Add New Record**
6. For each A record:
   - Type: **A Record**
   - Host: **@**
   - Value: Enter the IP address
   - TTL: **Automatic**
7. Add CNAME record:
   - Type: **CNAME Record**
   - Host: **www**
   - Value: **pawopawan.github.io.**
   - TTL: **Automatic**
8. Click **Save All Changes**
9. Wait 30 minutes for propagation

</details>

<details>
<summary><b>Cloudflare</b></summary>

1. Go to: https://dash.cloudflare.com/
2. Log in to your account
3. Select **br27.in** domain
4. Click **DNS** in the left sidebar
5. Click **Add record** for each:
   - Type: **A**
   - Name: **@**
   - IPv4 address: Enter the IP
   - Proxy status: **Proxied** (orange cloud)
   - TTL: **Auto**
6. Add CNAME:
   - Type: **CNAME**
   - Name: **www**
   - Target: **pawopawan.github.io**
   - Proxy status: **Proxied** (orange cloud)
7. Click **Save**
8. Propagation is usually instant with Cloudflare!

**Note:** If using Cloudflare, also ensure:
- SSL/TLS mode is set to **Full** or **Full (strict)**
- Under **SSL/TLS > Edge Certificates**, enable **Always Use HTTPS**

</details>

<details>
<summary><b>Google Domains</b></summary>

1. Go to: https://domains.google.com/
2. Click on **br27.in**
3. Click **DNS** in the left menu
4. Scroll to **Custom records**
5. Click **Manage custom records**
6. Click **Create new record**
7. For each A record:
   - Host name: **@**
   - Type: **A**
   - TTL: **3600**
   - Data: Enter the IP address
8. Add CNAME:
   - Host name: **www**
   - Type: **CNAME**
   - TTL: **3600**
   - Data: **pawopawan.github.io.**
9. Click **Save**
10. Wait 5-60 minutes for propagation

</details>

<details>
<summary><b>Hostinger</b></summary>

1. Go to: https://hpanel.hostinger.com/
2. Go to **Domains**
3. Click on **br27.in**
4. Click **DNS / Name Servers**
5. Click **Manage** next to DNS Records
6. For each A record:
   - Click **Add Record**
   - Type: **A**
   - Name: **@**
   - Points to: Enter the IP
   - TTL: **3600**
7. Add CNAME:
   - Type: **CNAME**
   - Name: **www**
   - Points to: **pawopawan.github.io.**
8. Click **Add Record** after each
9. Wait 15-60 minutes

</details>

<details>
<summary><b>Other Providers (Generic Steps)</b></summary>

1. Log into your domain registrar's website
2. Find **DNS Management** or **DNS Settings** or **Name Server Management**
3. Look for **Add Record** or **Manage DNS Records**
4. Add the 4 A records and 1 CNAME record as shown above
5. Save changes
6. Wait for DNS propagation (15 minutes to 48 hours)

</details>

---

## ✅ Verification Steps

### 1. Check DNS Propagation Online

Use these tools to verify your DNS records are set correctly:

- **Check A Records:**
  - Visit: https://www.whatsmydns.net/#A/br27.in
  - Should show all 4 GitHub IP addresses

- **Check CNAME Record:**
  - Visit: https://www.whatsmydns.net/#CNAME/www.br27.in
  - Should show: pawopawan.github.io

### 2. Command Line Check (Optional)

```bash
# Check A records
dig br27.in +short

# Check CNAME record
dig www.br27.in +short

# Check from specific DNS server
nslookup br27.in 8.8.8.8
```

### 3. Test in Browser

After DNS propagates (usually 30-120 minutes):
- Visit: http://br27.in (should redirect to https)
- Visit: https://br27.in (should load your site)
- Visit: https://www.br27.in (should redirect to br27.in)

---

## ⏱️ DNS Propagation Timeline

| Provider | Typical Time |
|----------|--------------|
| Cloudflare | 1-5 minutes |
| Google Domains | 5-15 minutes |
| Namecheap | 30 minutes |
| GoDaddy | 30-60 minutes |
| Others | 1-2 hours (max 48 hours) |

**Note:** Even if it says 48 hours maximum, it usually works within 1-2 hours!

---

## 🔍 Where to Find Your Domain Registrar

Not sure where you bought br27.in? Check:

1. **Email Confirmation:**
   - Search your email for "br27.in"
   - Look for purchase confirmation

2. **WHOIS Lookup:**
   - Visit: https://www.whois.com/whois/br27.in
   - Look for "Registrar" field

3. **Common Indian Registrars:**
   - GoDaddy India
   - Namecheap
   - BigRock
   - ResellerClub
   - Domain.com
   - Hostinger

---

## 🆘 Troubleshooting

### Problem: "I can't find DNS settings"

**Look for these menu names:**
- DNS Management
- DNS Settings
- DNS Records
- Name Servers
- Advanced DNS
- DNS Zone Editor
- Manage DNS

### Problem: "It says NS records are being used"

**Solution:**
- You might be using custom name servers
- Change to your registrar's default name servers first
- Then add the A and CNAME records

### Problem: "Old A records exist"

**Solution:**
- Delete old A records pointing to different IPs
- Add the new GitHub Pages IP addresses
- Keep only the 4 GitHub IPs

### Problem: "CNAME conflicts with A record"

**Solution:**
- You cannot have both CNAME and A records for the same name
- Keep A records for @ (apex domain)
- Keep CNAME only for www

---

## 📞 Need Help?

### Can't Access DNS Settings?

Contact your domain registrar's support:
- Most have 24/7 live chat
- Provide them this list of records
- They can add them for you

### GitHub Pages Not Working?

First ensure:
1. GitHub Pages is enabled: https://github.com/pawoPawan/BR27/settings/pages
2. Custom domain is set to **br27.in**
3. "Enforce HTTPS" is checked
4. Green checkmark shows "Your site is live"

---

## 🎯 Final Checklist

After DNS setup, verify:
- [ ] 4 A records added correctly
- [ ] 1 CNAME record added correctly
- [ ] Waited at least 30 minutes
- [ ] https://www.whatsmydns.net shows correct IPs
- [ ] GitHub Pages shows "DNS check successful"
- [ ] HTTPS is enforced
- [ ] br27.in loads your website
- [ ] www.br27.in redirects properly

---

## 📧 Quick Copy-Paste for Support

If you need to contact support, copy this:

```
Hi, I need to set up DNS records for my domain br27.in to point to GitHub Pages.

Please add these A records:
- Type: A, Name: @, Value: 185.199.108.153
- Type: A, Name: @, Value: 185.199.109.153
- Type: A, Name: @, Value: 185.199.110.153
- Type: A, Name: @, Value: 185.199.111.153

And this CNAME record:
- Type: CNAME, Name: www, Value: pawopawan.github.io.

Thank you!
```

---

## 🔐 Important GitHub Pages Settings

After DNS is configured, in GitHub:

1. Go to: https://github.com/pawoPawan/BR27/settings/pages
2. Under "Custom domain": **br27.in**
3. Wait for "DNS check successful" ✓
4. Check "Enforce HTTPS" ✓
5. Wait 10-30 minutes for HTTPS certificate

---

**🎉 Once DNS propagates, your website will be live at https://br27.in!**

Your bilingual (English/Hindi) BR27 website with all features will be accessible worldwide! 🌍

