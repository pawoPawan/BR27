# LinkedIn Feed Component

A modular LinkedIn feed component that automatically fetches posts from your LinkedIn company page.

## 🎯 Works on GitHub Pages!

This component has **3 modes**:

### 1. **Client-Side Auto-Fetch** (✅ Works on GitHub Pages)
```javascript
// Automatically fetches from LinkedIn RSS in browser
new LinkedInFeedClient('linkedin-feed-container', {
    postsToShow: 3,
    companyUrl: 'https://www.linkedin.com/company/27br/',
    carousel: true
});
```

### 2. **Static Mode** (✅ Works on GitHub Pages)
```javascript
// Uses static JSON file
new LinkedInFeed('linkedin-feed-container', {
    postsToShow: 3,
    dataSource: '/components/linkedin-feed/data/posts.json'
});
```

### 3. **Dynamic Server Mode** (❌ Needs separate backend)
```javascript
// Requires Django backend deployed separately
new LinkedInFeedDynamic('linkedin-feed-container', {
    dataSource: 'https://your-backend.herokuapp.com/api/linkedin/posts/'
});
```

---

## 🚀 Quick Start (Auto-Fetch on GitHub Pages)

```html
<!-- Include CSS -->
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed-carousel.css">

<!-- HTML Container -->
<div id="linkedin-feed-container"></div>

<!-- Include Script -->
<script src="/components/linkedin-feed/linkedin-feed-client.js"></script>
<script>
    // Auto-fetches from LinkedIn!
    new LinkedInFeedClient('linkedin-feed-container', {
        postsToShow: 3,
        companyUrl: 'https://www.linkedin.com/company/27br/',
        carousel: true,
        autoRefresh: true
    });
</script>
```

---

## ⚙️ Configuration

```javascript
new LinkedInFeedClient('container-id', {
    postsToShow: 3,                     // Number of posts
    companyUrl: 'https://www.linkedin.com/company/27br/',
    carousel: true,                     // Enable carousel
    carouselInterval: 5000,             // Rotate every 5 seconds
    autoRefresh: true,                  // Auto-refresh posts
    refreshInterval: 300000,            // Refresh every 5 minutes
    fallbackData: '/components/linkedin-feed/data/posts.json'
});
```

---

## 📦 Files

```
linkedin-feed/
├── linkedin-feed-client.js    # ✅ Auto-fetch (GitHub Pages)
├── linkedin-feed.js           # Static mode
├── linkedin-feed-dynamic.js   # Server mode
├── linkedin-feed.css          # Base styles
├── linkedin-feed-carousel.css # Carousel styles
└── data/posts.json            # Fallback data
```

---

## 🎯 How It Works

1. **Tries to fetch** from LinkedIn RSS via RSS2JSON API
2. **If successful**: Shows live LinkedIn posts
3. **If fails**: Uses fallback data from `posts.json`
4. **Auto-refreshes** every 5 minutes (optional)

---

## 📝 Documentation

- **Quick Start**: `docs/QUICK_START.md`
- **Integration Guide**: `docs/INTEGRATION_GUIDE.md`
- **Dynamic Setup**: `DYNAMIC_SETUP_GUIDE.md`

---

**Recommended**: Use `linkedin-feed-client.js` for automatic fetching on GitHub Pages!
