# DNS Configuration for www.br27.in and br27.in Access

## Current Setup
✅ CNAME file: `br27.in` (correct - apex domain)
✅ Repository: pawoPawan/BR27
✅ GitHub Pages: Enabled

## Required DNS Records on GoDaddy

### For GoDaddy DNS Manager, you need these exact records:

#### 1. A Records (for br27.in - apex domain)
| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | 185.199.108.153 | 600 seconds |
| A | @ | 185.199.109.153 | 600 seconds |
| A | @ | 185.199.110.153 | 600 seconds |
| A | @ | 185.199.111.153 | 600 seconds |

#### 2. CNAME Record (for www.br27.in - www subdomain)
| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | br27.in | 1 Hour |

**Alternative CNAME Value:** You can also use `pawopawan.github.io` instead of `br27.in`

## How to Verify DNS Setup

### Check A Records (apex domain)
```bash
dig br27.in +short
# Should return all 4 GitHub IPs:
# 185.199.108.153
# 185.199.109.153
# 185.199.110.153
# 185.199.111.153
```

### Check CNAME Record (www subdomain)
```bash
dig www.br27.in +short
# Should return: br27.in (or GitHub IPs if fully resolved)
```

### Check HTTPS
```bash
curl -I https://br27.in
curl -I https://www.br27.in
# Both should return: HTTP/2 200
```

## GitHub Pages Settings

1. Go to: https://github.com/pawoPawan/BR27/settings/pages
2. Verify:
   - ✅ Custom domain: `br27.in`
   - ✅ Enforce HTTPS: **ENABLED** (check this box!)
3. If "Enforce HTTPS" is unavailable:
   - Remove `br27.in` from custom domain
   - Save
   - Wait 30 seconds
   - Re-add `br27.in`
   - Save
   - Wait 5-10 minutes for SSL certificate

## Expected Behavior

Once DNS propagates (up to 48 hours, usually 30 minutes):

✅ `https://br27.in` → Works (main site)
✅ `http://br27.in` → Redirects to https://br27.in
✅ `https://www.br27.in` → Works (redirects to https://br27.in OR shows site directly)
✅ `http://www.br27.in` → Redirects to https://www.br27.in then to https://br27.in
✅ `www.br27.in` → Automatically uses HTTPS

## Troubleshooting

### If www.br27.in doesn't work:
1. Verify CNAME record exists: `dig www.br27.in +short`
2. Check GoDaddy DNS - ensure CNAME for `www` points to `br27.in` or `pawopawan.github.io`
3. Wait for DNS propagation (use https://dnschecker.org)

### If HTTPS isn't working:
1. In GitHub Pages settings, try removing and re-adding custom domain
2. Wait 5-10 minutes for SSL certificate provisioning
3. Enable "Enforce HTTPS" checkbox

### If nothing works:
1. Verify GitHub Pages is enabled in repository settings
2. Check that main branch is selected as source
3. Verify CNAME file exists in root directory with `br27.in`
4. Check repository visibility is Public

## DNS Propagation Check

Check if DNS has propagated worldwide:
- Visit: https://dnschecker.org
- Enter: `br27.in` (for A records)
- Enter: `www.br27.in` (for CNAME record)
- Should show green checkmarks across all locations

## Summary

Your current setup is correct:
- ✅ CNAME file has `br27.in`
- ✅ Need to verify GoDaddy DNS has:
  - 4 A records for @ → GitHub IPs
  - 1 CNAME record for www → br27.in

Once DNS is correct, GitHub Pages automatically handles:
- HTTP → HTTPS redirects
- www ↔ non-www redirects
- SSL certificate for both
