# Dynamic LinkedIn Feed Setup Guide

## 🎯 What's New

Your LinkedIn feed now **dynamically fetches posts from LinkedIn** and displays them in a **rotating carousel**!

### ✨ Features
- ✅ **Auto-fetch from LinkedIn** - No manual JSON updates
- ✅ **3-post rotating carousel** - Auto-rotates every 5 seconds
- ✅ **Auto-refresh** - Updates every 5 minutes
- ✅ **Dedicated articles page** - Shows all LinkedIn posts
- ✅ **Fallback system** - Uses cached data if LinkedIn API is unavailable
- ✅ **Django backend API** - RESTful endpoint for posts

---

## 📦 New Files Created

```
/django/linkedin_feed/              # Django app for LinkedIn API
├── __init__.py
├── views.py                        # API endpoints
└── urls.py                         # URL routing

/components/linkedin-feed/
├── linkedin-feed-dynamic.js        # Enhanced JS with carousel
├── linkedin-feed-carousel.css      # Carousel styles
└── examples/
    └── dynamic-carousel-integration.html

/linkedin-articles.html             # Dedicated articles page
```

---

## 🚀 Quick Setup

### 1. Update Django settings

Edit `/django/drone_website/settings.py` (already done):
- LinkedIn feed app URL routing added

### 2. Add CSS to your page

```html
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed-carousel.css">
```

### 3. Add HTML section

```html
<section class="linkedin-feed-section">
    <div class="container">
        <div class="linkedin-header">
            <!-- Header content -->
        </div>
        <div id="linkedin-feed-container"></div>
    </div>
</section>
```

### 4. Add JavaScript

```html
<script src="/components/linkedin-feed/linkedin-feed-dynamic.js"></script>
<script>
    new LinkedInFeedDynamic('linkedin-feed-container', {
        postsToShow: 3,                    // Show 3 posts
        dataSource: '/api/linkedin/posts/', // Django API endpoint
        carousel: true,                     // Enable carousel
        carouselInterval: 5000,             // Rotate every 5 seconds
        autoRefresh: true,                  // Auto-refresh
        refreshInterval: 300000             // Refresh every 5 minutes
    });
</script>
```

---

## 🎨 How It Works

### Architecture

```
LinkedIn → RSS2JSON Service → Django API → Frontend Component → Browser
                                   ↓
                            Fallback to JSON file if unavailable
```

### Data Flow

1. **Frontend** requests posts from `/api/linkedin/posts/`
2. **Django backend** fetches from LinkedIn RSS via RSS2JSON
3. If successful, returns fresh data
4. If unavailable, returns cached data from `data/posts.json`
5. **Frontend** displays in rotating carousel
6. Auto-refreshes every 5 minutes

---

## 🔌 API Endpoints

### GET `/api/linkedin/posts/`

Fetch LinkedIn posts

**Query Parameters:**
- `count` (optional): Number of posts (default: 10, max: 20)

**Response:**
```json
{
  "success": true,
  "count": 3,
  "posts": [
    {
      "id": 1,
      "title": "Post Title",
      "excerpt": "Brief description...",
      "description": "Full text...",
      "date": "2025-11-28",
      "url": "https://linkedin.com/...",
      "image": null,
      "author": "BR27",
      "categories": []
    }
  ],
  "lastUpdated": "2025-11-28T10:00:00",
  "source": "linkedin-rss"
}
```

### GET `/api/linkedin/status/`

Check LinkedIn feed connection status

**Response:**
```json
{
  "status": "connected",
  "service": "rss2json",
  "message": "LinkedIn feed is accessible"
}
```

---

## 🎯 Integration Examples

### Example 1: Home Page with Carousel

```html
<!-- home.html -->
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed.css">
<link rel="stylesheet" href="/components/linkedin-feed/linkedin-feed-carousel.css">

<section class="linkedin-feed-section">
    <div class="container">
        <div id="linkedin-feed-container"></div>
    </div>
</section>

<script src="/components/linkedin-feed/linkedin-feed-dynamic.js"></script>
<script>
    new LinkedInFeedDynamic('linkedin-feed-container', {
        postsToShow: 3,
        carousel: true,
        autoRefresh: true
    });
</script>
```

### Example 2: Articles Page (All Posts)

Visit: `/linkedin-articles.html`

Shows all available LinkedIn posts with:
- Filter tabs (All, Recent, Popular)
- Grid layout
- Load more pagination
- Links back to LinkedIn

---

## ⚙️ Configuration Options

```javascript
new LinkedInFeedDynamic('container-id', {
    // Number of posts to show
    postsToShow: 3,
    
    // API endpoint
    dataSource: '/api/linkedin/posts/',
    
    // Carousel settings
    carousel: true,                 // Enable/disable carousel
    carouselInterval: 5000,         // Rotate every 5 seconds
    
    // Auto-refresh settings
    autoRefresh: true,              // Enable/disable auto-refresh
    refreshInterval: 300000,        // Refresh every 5 minutes
    
    // Display settings
    showEngagement: true            // Show likes/comments (if available)
});
```

---

## 🔧 Fallback System

The system has 3 levels of fallback:

1. **Primary**: Fetch from LinkedIn via RSS2JSON
2. **Secondary**: Use cached data from `data/posts.json`
3. **Tertiary**: Use hardcoded sample data

This ensures the feed always displays something, even if LinkedIn is unavailable.

---

## 🎨 Carousel Features

- **Auto-rotate**: Changes slides every 5 seconds
- **Manual navigation**: Previous/Next buttons
- **Dot indicators**: Click to jump to specific slide
- **Pause on hover**: Carousel pauses when you hover over it
- **Smooth transitions**: Fade and slide animations
- **Responsive**: Works on all screen sizes

---

## 📱 Responsive Design

- **Desktop**: Full carousel with large cards
- **Tablet**: Medium-sized carousel
- **Mobile**: Adjusted buttons and spacing

---

## 🧪 Testing

### 1. Test API Endpoint

```bash
# Start Django server
cd django
python manage.py runserver

# Test in browser or curl
curl http://localhost:8000/api/linkedin/posts/?count=3
```

### 2. Test Frontend

```bash
# Start local server
cd /path/to/br27
./setup.sh start

# Open in browser
http://localhost:8000/home.html
```

### 3. Test Articles Page

```
http://localhost:8000/linkedin-articles.html
```

---

## 🔍 Troubleshooting

### Posts not loading

1. **Check Django server is running**
   ```bash
   cd django && python manage.py runserver
   ```

2. **Check API endpoint**
   - Visit: `http://localhost:8000/api/linkedin/posts/`
   - Should return JSON data

3. **Check browser console**
   - Press F12
   - Look for error messages

### Carousel not working

1. **Check CSS is loaded**
   - Both `linkedin-feed.css` and `linkedin-feed-carousel.css`

2. **Check JavaScript**
   - `linkedin-feed-dynamic.js` (not the old `linkedin-feed.js`)

3. **Check container ID**
   - Must match: `linkedin-feed-container`

### RSS2JSON Service Issues

If RSS2JSON is down or limited:
- System automatically falls back to cached data
- Update `data/posts.json` manually as backup

---

## 📊 Performance

- **API cache**: 15 minutes (Django level)
- **Frontend refresh**: 5 minutes (configurable)
- **Fallback**: Instant (no external calls)
- **Carousel**: Smooth 60fps animations

---

## 🚀 Deployment

### 1. Update requirements.txt

```bash
cd django
pip install requests
pip freeze > requirements.txt
```

### 2. Configure for production

In `django/drone_website/settings.py`:
```python
# Production settings
DEBUG = False
ALLOWED_HOSTS = ['br27.in', 'www.br27.in']
```

### 3. Collect static files

```bash
python manage.py collectstatic
```

### 4. Deploy

```bash
# Commit all changes
git add .
git commit -m "Add dynamic LinkedIn feed with carousel"
git push
```

---

## 📝 Manual Updates (Backup)

If you want to manually update posts:

```bash
cd components/linkedin-feed/scripts
python3 update-posts.py
```

This updates `data/posts.json` which serves as fallback data.

---

## 🎯 Summary

**What you now have:**

1. ✅ **Dynamic fetching** from LinkedIn
2. ✅ **Auto-rotating carousel** (3 posts, 5-second intervals)
3. ✅ **Auto-refresh** (every 5 minutes)
4. ✅ **Dedicated articles page** (`/linkedin-articles.html`)
5. ✅ **Django REST API** (`/api/linkedin/posts/`)
6. ✅ **Fallback system** (3-level redundancy)
7. ✅ **Responsive design** (all devices)

**No more manual JSON updates - it's all automatic!** 🎉

---

## 🔗 Quick Links

- **Articles Page**: `/linkedin-articles.html`
- **API Endpoint**: `/api/linkedin/posts/`
- **API Status**: `/api/linkedin/status/`
- **Example**: `/components/linkedin-feed/examples/dynamic-carousel-integration.html`

---

## 📚 Related Documentation

- **Module Overview**: `MODULE_INFO.md`
- **Quick Start**: `docs/QUICK_START.md`
- **Integration Guide**: `docs/INTEGRATION_GUIDE.md`

---

**Your LinkedIn feed is now fully dynamic with auto-updating carousel!** 🚀

