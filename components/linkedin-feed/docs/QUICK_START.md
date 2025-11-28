# 🚀 LinkedIn Feed - Quick Start

## Module Location
```
/components/linkedin-feed/
```

All files are self-contained in this directory. No scattered files!

---

## 📦 What's Inside

```
linkedin-feed/
├── linkedin-feed.css          # Styles
├── linkedin-feed.js           # Logic
├── data/
│   └── posts.json            # Your LinkedIn posts data
├── examples/
│   ├── demo.html             # Live demo
│   ├── integration-example.html
│   └── section-snippet.html  # Copy-paste snippet
├── docs/
│   ├── README.md             # Main documentation
│   ├── QUICK_START.md        # This file
│   └── INTEGRATION_GUIDE.md  # Detailed guide
└── scripts/
    └── update-posts.py       # Post manager
```

---

## ⚡ 3-Step Integration

### Step 1: Add CSS (in `<head>`)

```html
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">
```

### Step 2: Add HTML (where you want the feed)

```html
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
               class="linkedin-follow-btn">
                Follow on LinkedIn
            </a>
        </div>
        <div id="linkedin-feed-container"></div>
    </div>
</section>
```

### Step 3: Add JavaScript (before `</body>`)

```html
<script src="/components/linkedin-feed/linkedin-feed.js"></script>
<script>
    document.addEventListener('DOMContentLoaded', function() {
        new LinkedInFeed('linkedin-feed-container', {
            postsToShow: 6,
            dataSource: '/components/linkedin-feed/data/posts.json'
        });
    });
</script>
```

---

## 🎯 Path Reference

### For Root Pages (`/home.html`)
```html
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">
<script src="/components/linkedin-feed/linkedin-feed.js"></script>
<script>
    new LinkedInFeed('linkedin-feed-container', {
        dataSource: '/components/linkedin-feed/data/posts.json'
    });
</script>
```

### For Focus Area Pages (`/focus-areas/*/index.html`)
```html
<link rel="stylesheet" href="../../components/linkedin-feed/linkedin-feed.css">
<script src="../../components/linkedin-feed/linkedin-feed.js"></script>
<script>
    new LinkedInFeed('linkedin-feed-container', {
        dataSource: '../../components/linkedin-feed/data/posts.json',
        postsToShow: 3  // Show fewer on internal pages
    });
</script>
```

---

## 📝 Update Posts

### Option 1: Interactive Script
```bash
cd components/linkedin-feed/scripts
python3 update-posts.py
```

### Option 2: Edit JSON Directly
```bash
nano components/linkedin-feed/data/posts.json
```

### Option 3: Generate Sample Posts
```bash
cd components/linkedin-feed/scripts
python3 update-posts.py --sample
```

---

## 🎨 View Demo

```bash
# Open demo file
open components/linkedin-feed/examples/demo.html

# Or with local server
http://localhost:8000/components/linkedin-feed/examples/demo.html
```

---

## ⚙️ Configuration Options

```javascript
new LinkedInFeed('linkedin-feed-container', {
    postsToShow: 6,              // Number of posts to display
    dataSource: '/components/linkedin-feed/data/posts.json',
    showEngagement: true,        // Show likes and comments
    autoRefresh: false,          // Auto-refresh posts
    refreshInterval: 300000      // Refresh every 5 minutes (ms)
});
```

---

## 🔧 Customization

Edit styles in:
```
/components/linkedin-feed/linkedin-feed.css
```

Colors, spacing, and layout can all be customized there.

---

## 📚 More Documentation

- **Full README**: `docs/README.md`
- **Integration Guide**: `docs/INTEGRATION_GUIDE.md`
- **Examples**: Check `examples/` folder

---

## ✅ Quick Checklist

- [ ] CSS included in `<head>`
- [ ] HTML section added where you want it
- [ ] JavaScript included before `</body>`
- [ ] Correct path to `data/posts.json`
- [ ] Container ID matches (`linkedin-feed-container`)

---

**That's it! Your LinkedIn feed should now be working.** 🎉

For issues, check browser console (F12) for error messages.
