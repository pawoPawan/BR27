# LinkedIn Feed Module for BR27 Website

A modular, self-contained component to display LinkedIn posts on your website.

## 📦 Module Structure

```
components/linkedin-feed/
├── linkedin-feed.css          # Component styles
├── linkedin-feed.js           # Component logic
├── data/
│   └── posts.json            # LinkedIn posts data
├── examples/
│   ├── demo.html             # Live demo
│   ├── integration-example.html
│   └── section-snippet.html  # HTML snippet
├── docs/
│   ├── README.md             # This file
│   ├── QUICK_START.md        # Quick reference
│   └── INTEGRATION_GUIDE.md  # Detailed guide
└── scripts/
    └── update-posts.py       # Post management script
```

## 🚀 Quick Start

### 1. Include in Your Page

```html
<!-- In <head> -->
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">

<!-- Where you want the feed -->
<div id="linkedin-feed-container"></div>

<!-- Before </body> -->
<script src="/components/linkedin-feed/linkedin-feed.js"></script>
<script>
    new LinkedInFeed('linkedin-feed-container', {
        postsToShow: 6,
        dataSource: '/components/linkedin-feed/data/posts.json'
    });
</script>
```

### 2. Update Posts

```bash
# Interactive update
cd components/linkedin-feed/scripts
python3 update-posts.py

# Or edit directly
nano components/linkedin-feed/data/posts.json
```

### 3. View Demo

```bash
# Open demo
open components/linkedin-feed/examples/demo.html

# Or with server
http://localhost:8000/components/linkedin-feed/examples/demo.html
```

## 📚 Documentation

- **Quick Start**: See `docs/QUICK_START.md` for fast setup
- **Integration Guide**: See `docs/INTEGRATION_GUIDE.md` for detailed instructions
- **Examples**: Check `examples/` folder for working examples

## ⚙️ Configuration

```javascript
new LinkedInFeed('container-id', {
    postsToShow: 6,              // Number of posts
    dataSource: '/components/linkedin-feed/data/posts.json',
    showEngagement: true,        // Show likes/comments
    autoRefresh: false,          // Auto-refresh posts
    refreshInterval: 300000      // Refresh interval (ms)
});
```

## 🎯 Integration Examples

### For Root Pages (home.html)

```html
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">
<script src="/components/linkedin-feed/linkedin-feed.js"></script>
<script>
    new LinkedInFeed('linkedin-feed-container', {
        dataSource: '/components/linkedin-feed/data/posts.json'
    });
</script>
```

### For Focus Area Pages (focus-areas/*/index.html)

```html
<link rel="stylesheet" href="../../components/linkedin-feed/linkedin-feed.css">
<script src="../../components/linkedin-feed/linkedin-feed.js"></script>
<script>
    new LinkedInFeed('linkedin-feed-container', {
        dataSource: '../../components/linkedin-feed/data/posts.json',
        postsToShow: 3
    });
</script>
```

## 📝 Features

- ✅ Self-contained module
- ✅ No external dependencies
- ✅ Responsive design
- ✅ Easy integration
- ✅ Customizable styling
- ✅ Sample data included

## 🔧 Customization

All styles are in `linkedin-feed.css`. Customize colors, spacing, and layout as needed.

## 📄 License

Part of BR27 website project.

---

**For detailed documentation, see `docs/` folder.**

