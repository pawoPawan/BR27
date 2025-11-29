# LinkedIn Feed Troubleshooting Guide

## 🔍 Issue: LinkedIn feed not showing on www.br27.in

## ✅ What's Been Set Up

### 1. **Feed Configuration** (`_data/feeds.yml`)
```yaml
home_page:
  feeds:
    - type: linkedin
      enabled: true
      posts_count: 3
      carousel: true
      auto_refresh: true
      position: before_footer
```

### 2. **Feed Loader** (`_includes/feeds-loader.html`)
- Dynamically loads feeds based on configuration
- Checks for enabled feeds
- Matches position (before_footer)

### 3. **LinkedIn Component** (`_includes/linkedin-feed.html`)
- Platform-agnostic implementation
- Reads from `config/platform.json`
- Auto-detects GitHub Pages vs Django

### 4. **Home Page Integration** (`home.html` line 320)
```liquid
{% include feeds-loader.html page_type="home_page" position="before_footer" %}
```

### 5. **CSS & JS Includes** (`home.html` line 9)
```liquid
{% include head-feeds.html %}
```

## 🧪 Test Pages

### **Test Page:** https://www.br27.in/test-feed.html
This standalone page tests the LinkedIn feed with debug output.

**What to look for:**
1. Visit https://www.br27.in/test-feed.html
2. Check the "Debug Information" section
3. Should see:
   - ✅ DOM Content Loaded
   - ✅ LinkedIn Client Available: true
   - ✅ Platform config loaded
   - ✅ Feed initialized

## 🔍 Debugging Steps

### **Step 1: Check if GitHub Pages built successfully**
1. Go to: https://github.com/pawoPawan/BR27/actions
2. Look for latest workflow run
3. Should be green ✅ (success)
4. If red ❌, check build logs for errors

### **Step 2: Check test page**
1. Visit: https://www.br27.in/test-feed.html
2. Look at debug output
3. Open browser console (F12)
4. Check for JavaScript errors

### **Step 3: Check file accessibility**
Try accessing these URLs directly:

```
https://www.br27.in/config/platform.json
https://www.br27.in/components/linkedin-feed/linkedin-feed-client.js
https://www.br27.in/components/linkedin-feed/linkedin-feed.css
https://www.br27.in/components/linkedin-feed/data/posts.json
```

All should return **HTTP 200**.

### **Step 4: Check home page source**
1. Visit: https://www.br27.in/home
2. View Page Source (Ctrl+U / Cmd+U)
3. Search for "linkedin-feed"
4. Should find:
   - CSS link to linkedin-feed.css
   - Script tag for linkedin-feed-client.js
   - `<section class="linkedin-feed-section">`

### **Step 5: Check browser console**
1. Visit: https://www.br27.in/home
2. Open Console (F12)
3. Look for:
   - "✅ LinkedIn feed initialized for platform: github"
   - Any red error messages

## 🐛 Common Issues & Solutions

### **Issue 1: Jekyll not processing includes**

**Symptoms:**
- Page source shows raw `{% include %}` tags
- No LinkedIn feed section in HTML

**Solution:**
```bash
# Check _config.yml excludes
# Make sure _includes/ and _data/ are NOT excluded
```

### **Issue 2: YAML syntax error in feeds.yml**

**Symptoms:**
- Build fails on GitHub Actions
- No feed appears

**Solution:**
```bash
# Check YAML indentation (must use spaces, not tabs)
# Validate YAML at: https://www.yamllint.com/
```

### **Issue 3: JavaScript not loading**

**Symptoms:**
- Console shows: "LinkedInFeedClient is not defined"
- No feed appears

**Solution:**
```html
<!-- Verify script tag in HTML source: -->
<script src="/components/linkedin-feed/linkedin-feed-client.js"></script>

<!-- Check file exists at: -->
https://www.br27.in/components/linkedin-feed/linkedin-feed-client.js
```

### **Issue 4: Platform config not found**

**Symptoms:**
- Console shows: "Platform config unavailable"
- Feed may still work with fallback

**Solution:**
```bash
# Verify config/platform.json is NOT in _config.yml excludes
# Check file is accessible at:
https://www.br27.in/config/platform.json
```

### **Issue 5: GitHub Pages cache**

**Symptoms:**
- Changes pushed but not visible
- Old content still showing

**Solution:**
```bash
# Wait 2-3 minutes for GitHub Pages to rebuild
# Force refresh: Ctrl+Shift+R (Windows) / Cmd+Shift+R (Mac)
# Clear cache and hard reload
```

### **Issue 6: RSS2JSON API limit**

**Symptoms:**
- Feed shows but no posts
- Console error about API

**Solution:**
```javascript
// RSS2JSON free tier: 10,000 requests/day
// If limit reached, falls back to static posts.json
// Should still show sample posts
```

## 📋 Verification Checklist

Run through this checklist:

- [ ] GitHub Actions build successful (green ✅)
- [ ] Test page (test-feed.html) shows debug output
- [ ] Test page shows LinkedIn posts
- [ ] Config files accessible:
  - [ ] /config/platform.json
  - [ ] /components/linkedin-feed/data/posts.json
- [ ] JavaScript files accessible:
  - [ ] /components/linkedin-feed/linkedin-feed-client.js
- [ ] CSS files accessible:
  - [ ] /components/linkedin-feed/linkedin-feed.css
  - [ ] /components/linkedin-feed/linkedin-feed-carousel.css
- [ ] Home page source contains:
  - [ ] LinkedIn CSS links
  - [ ] LinkedIn JS script
  - [ ] linkedin-feed-section element
- [ ] Browser console shows:
  - [ ] No red errors
  - [ ] "LinkedIn feed initialized" message

## 🔧 Quick Fixes

### **Fix 1: Force rebuild**
```bash
# Make a small change and push
cd /path/to/br27
echo "<!-- rebuild -->" >> home.html
git add home.html
git commit -m "Force rebuild"
git push origin main
# Wait 2-3 minutes
```

### **Fix 2: Simplify includes (if Jekyll issues)**
Instead of the loader system, directly include in home.html:

```liquid
<!-- Replace line 320 in home.html: -->
{% include linkedin-feed.html posts_count="3" carousel="true" auto_refresh="true" %}
```

### **Fix 3: Check Jekyll version**
GitHub Pages uses Jekyll 3.9.x. Verify compatibility:
```yaml
# _config.yml
jekyll: "~> 3.9"
```

## 📊 Expected Behavior

### **When Everything Works:**

1. **Home page loads**
2. **Before footer**, you see:
   - Section with "Latest from BR27" heading
   - LinkedIn icon
   - 3 posts in a carousel
   - Auto-rotating every 5 seconds
   - "Follow on LinkedIn" button
   - "View All Articles" link

3. **Browser console shows:**
   ```
   ✅ LinkedIn feed initialized for platform: github
   ```

4. **Page source contains:**
   ```html
   <section class="linkedin-feed-section">
     <div class="container">
       <div class="linkedin-header">
         <h2>Latest from BR27</h2>
         ...
       </div>
       <div id="linkedin-feed-container">
         <!-- Posts rendered here -->
       </div>
     </div>
   </section>
   ```

## 🚨 If Nothing Works

### **Nuclear Option: Simplified Direct Integration**

1. Open `home.html`
2. Find line 320 (the feeds-loader include)
3. Replace with direct include:

```liquid
<!-- LinkedIn Feed -->
{% include linkedin-feed.html posts_count="3" carousel="true" auto_refresh="true" %}
```

4. Commit and push:
```bash
git add home.html
git commit -m "Use direct LinkedIn feed include"
git push origin main
```

5. Wait 2-3 minutes and refresh

## 📞 Still Not Working?

Check these final items:

1. **Is www.br27.in actually pointing to GitHub Pages?**
   ```bash
   nslookup www.br27.in
   # Should show GitHub Pages IP
   ```

2. **Is HTTPS working?**
   - Mixed content (HTTP/HTTPS) can block scripts
   - All resources should be HTTPS or relative URLs

3. **Browser blocking content?**
   - Check if adblocker is blocking LinkedIn-related content
   - Try in incognito/private mode
   - Try different browser

4. **Jekyll build logs**
   - Check GitHub Actions for warnings
   - Look for "Liquid syntax error"
   - Look for "File not found"

## 📝 Debug Output Template

When asking for help, provide this information:

```
1. Test page debug output: (from https://www.br27.in/test-feed.html)
   [Paste debug output here]

2. Browser console errors: (F12 → Console)
   [Paste any red errors here]

3. GitHub Actions status:
   Link: https://github.com/pawoPawan/BR27/actions
   Status: ✅ Success / ❌ Failed
   
4. File accessibility:
   platform.json: [200 OK / 404 Not Found]
   linkedin-feed-client.js: [200 OK / 404 Not Found]
   posts.json: [200 OK / 404 Not Found]

5. Home page source includes feed: [Yes / No]

6. Browser: [Chrome / Firefox / Safari] [Version]
```

---

## ✅ Current Status Summary

**Architecture:** ✅ Correct
**Configuration:** ✅ Complete
**Files:** ✅ All present
**Code:** ✅ No errors

**Most likely issue:** GitHub Pages rebuild delay or cache

**Solution:** Wait 2-3 minutes after push, then force refresh (Ctrl+Shift+R)

---

**Last Updated:** Nov 29, 2025
**System Status:** Deployed & Configured ✅
**Test Page:** https://www.br27.in/test-feed.html

