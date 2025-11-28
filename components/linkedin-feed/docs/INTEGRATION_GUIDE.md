# LinkedIn Feed Component - Integration Guide

Complete guide to integrating the LinkedIn feed into your BR27 website.

---

## 📍 Module Location

**All files are in one place:**
```
/components/linkedin-feed/
```

No scattered files across the project!

---

## 🎯 Integration Scenarios

### Scenario 1: Home Page Integration

**File:** `/home.html`

**Add in `<head>` section:**
```html
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">
```

**Add before footer:**
```html
<!-- LinkedIn Feed Section -->
<section class="linkedin-feed-section">
    <div class="container">
        <div class="linkedin-header">
            <div class="linkedin-title-group">
                <div class="linkedin-icon">
                    <svg viewBox="0 0 24 24" fill="white" width="24" height="24">
                        <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                        <rect x="2" y="9" width="4" height="12"/>
                        <circle cx="4" cy="4" r="2"/>
                    </svg>
                </div>
                <div>
                    <h2>Latest from BR27</h2>
                    <p style="color: var(--text-secondary); margin: 0; font-size: 14px;">
                        Follow our journey on LinkedIn
                    </p>
                </div>
            </div>
            <a href="https://www.linkedin.com/company/27br/" 
               target="_blank" 
               rel="noopener noreferrer" 
               class="linkedin-follow-btn">
                Follow on LinkedIn
            </a>
        </div>
        <div id="linkedin-feed-container"></div>
    </div>
</section>
```

**Add before `</body>`:**
```html
<script src="/components/linkedin-feed/linkedin-feed.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        new LinkedInFeed('linkedin-feed-container', {
            postsToShow: 6,
            dataSource: '/components/linkedin-feed/data/posts.json',
            showEngagement: true
        });
    });
</script>
```

---

### Scenario 2: Focus Area Pages Integration

**Files:** `/focus-areas/education-careers/index.html`, etc.

**Note:** Use `../../` for relative paths!

**Add in `<head>` section:**
```html
<link rel="stylesheet" href="../../components/linkedin-feed/linkedin-feed.css">
```

**Add after CTA section, before footer:**
```html
<!-- LinkedIn Feed Section -->
<section class="linkedin-feed-section">
    <div class="container">
        <!-- Same HTML as above -->
        <div id="linkedin-feed-container"></div>
    </div>
</section>
```

**Add before `</body>`:**
```html
<script src="../../components/linkedin-feed/linkedin-feed.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        new LinkedInFeed('linkedin-feed-container', {
            postsToShow: 3,  // Show fewer posts on internal pages
            dataSource: '../../components/linkedin-feed/data/posts.json',
            showEngagement: true
        });
    });
</script>
```

---

### Scenario 3: Django Template Integration

**File:** `/django/templates/index.html`

**Add in `<head>`:**
```django
{% load static %}
<link rel="stylesheet" href="{% static 'components/linkedin-feed/linkedin-feed.css' %}">
```

**Add in body:**
```django
<section class="linkedin-feed-section">
    <!-- Same HTML structure -->
    <div id="linkedin-feed-container"></div>
</section>

<script src="{% static 'components/linkedin-feed/linkedin-feed.js' %}"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        new LinkedInFeed('linkedin-feed-container', {
            postsToShow: 6,
            dataSource: '{% static "components/linkedin-feed/data/posts.json" %}'
        });
    });
</script>
```

---

## 📝 Managing Posts

### Method 1: Interactive Python Script (Recommended)

```bash
# Navigate to scripts directory
cd components/linkedin-feed/scripts

# Run the updater
python3 update-posts.py

# Choose from menu:
# 1. View current posts
# 2. Add new post
# 3. Remove a post
# 4. Update engagement stats
# 5. Save and exit
```

### Method 2: Direct JSON Edit

```bash
# Edit the data file
nano components/linkedin-feed/data/posts.json
```

**JSON Structure:**
```json
{
  "posts": [
    {
      "id": 1,
      "title": "Your Post Title",
      "excerpt": "Brief description (150-200 characters)",
      "date": "2025-11-28",
      "url": "https://www.linkedin.com/posts/your-actual-post-url",
      "image": null,
      "likes": 150,
      "comments": 25
    }
  ],
  "lastUpdated": "2025-11-28"
}
```

### Method 3: Get Real LinkedIn Post URLs

1. Visit: https://www.linkedin.com/company/27br/
2. Click on a post you want to feature
3. Copy the URL from your browser address bar
4. Use that URL in the JSON `"url"` field

---

## ⚙️ Configuration Options

```javascript
new LinkedInFeed('container-id', {
    // Required
    dataSource: '/components/linkedin-feed/data/posts.json',
    
    // Optional (with defaults)
    postsToShow: 6,              // Number of posts to display
    showEngagement: true,        // Show likes and comments
    autoRefresh: false,          // Auto-refresh posts
    refreshInterval: 300000      // Refresh interval in milliseconds (5 min)
});
```

---

## 🎨 Customization

### Change Colors

Edit `/components/linkedin-feed/linkedin-feed.css`:

```css
/* LinkedIn button color */
.linkedin-follow-btn {
    background: linear-gradient(135deg, #0077b5 0%, #0e5a87 100%);
}

/* Post card hover effect */
.linkedin-post-card:hover {
    border-color: rgba(0, 119, 181, 0.3);
    box-shadow: 0 8px 30px rgba(0, 119, 181, 0.2);
}
```

### Change Grid Layout

```css
/* Number of columns */
.linkedin-posts-grid {
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    /* Change 320px to your preferred minimum width */
}
```

### Change Animation Speed

```css
/* Card animation delay */
.linkedin-post-card:nth-child(1) { animation-delay: 0.1s; }
.linkedin-post-card:nth-child(2) { animation-delay: 0.2s; }
/* Adjust delays as needed */
```

---

## 📱 Responsive Design

The component automatically adjusts:

- **Desktop (> 992px)**: 3 columns
- **Tablet (768px - 992px)**: 2 columns
- **Mobile (< 768px)**: 1 column

All styles are in one file: `linkedin-feed.css`

---

## 🔍 Testing

### 1. View Demo

```bash
# Start local server
./setup.sh start

# Open demo
http://localhost:8000/components/linkedin-feed/examples/demo.html
```

### 2. Test Integration

1. Add component to your page
2. Open page in browser
3. Open DevTools (F12)
4. Check Console tab for any errors
5. Verify posts are loading

### 3. Test Responsiveness

1. Open page in browser
2. Press F12 to open DevTools
3. Click device toggle (Ctrl+Shift+M)
4. Test different screen sizes

---

## 🆘 Troubleshooting

### Posts Not Showing

**Issue:** Container is empty

**Solutions:**
1. Check if `data/posts.json` exists
2. Verify path to JSON file is correct
3. Open browser console (F12) for error messages
4. Ensure container ID matches: `linkedin-feed-container`

### CSS Not Loading

**Issue:** No styling on component

**Solutions:**
1. Verify path to `linkedin-feed.css`
2. Clear browser cache (Ctrl+Shift+R / Cmd+Shift+R)
3. Check if CSS file exists in `/components/linkedin-feed/`
4. Inspect element to see if styles are applied

### JavaScript Errors

**Issue:** Console shows errors

**Solutions:**
1. Ensure `linkedin-feed.js` loads before initialization
2. Verify container element exists in HTML
3. Check data source path is correct
4. Validate JSON syntax at jsonlint.com

### Wrong Number of Posts

**Issue:** Showing incorrect number

**Solution:**
```javascript
// Adjust postsToShow value
new LinkedInFeed('linkedin-feed-container', {
    postsToShow: 6  // Change this number
});
```

---

## 📊 Best Practices

1. **Update Regularly**: Keep posts fresh (weekly/monthly)
2. **Real Data**: Use actual engagement numbers from LinkedIn
3. **Optimize Images**: Compress images if using them
4. **Test Mobile**: Always check on actual devices
5. **Monitor Performance**: Check load times in DevTools

---

## 🚀 Deployment

After integration:

```bash
# Commit changes
git add components/linkedin-feed/
git commit -m "Integrate LinkedIn feed component"

# Push to repository
git push origin main

# Or use deploy script
./deploy-github.sh "Add LinkedIn feed"
```

Changes will be live in 1-5 minutes on GitHub Pages.

---

## 📚 Additional Resources

- **Quick Start**: `docs/QUICK_START.md`
- **Main README**: `docs/README.md`
- **Examples**: `examples/` folder
- **BR27 LinkedIn**: https://www.linkedin.com/company/27br/

---

## ✅ Integration Checklist

Before going live, verify:

- [ ] CSS file linked correctly
- [ ] JavaScript file loaded
- [ ] Container element exists with correct ID
- [ ] Data source path is correct
- [ ] Posts display correctly
- [ ] Responsive on mobile
- [ ] Links open LinkedIn in new tab
- [ ] No console errors
- [ ] Sample data replaced with real posts

---

**Need help? Check the examples in the `examples/` folder for working implementations.**

All files are self-contained in `/components/linkedin-feed/` - no scattered files!
