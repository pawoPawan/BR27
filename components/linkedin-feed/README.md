# LinkedIn Feed Component

Modular component for displaying LinkedIn posts on BR27 website.

## 📦 Files

```
components/linkedin-feed/
├── linkedin-feed-client.js      # Main JavaScript (fetches from RSS2JSON)
├── linkedin-feed-compact.css    # Compact styling
├── data/
│   └── posts.json              # Fallback data (if API unavailable)
└── README.md                    # This file
```

## 🚀 Usage

The component is automatically included in `home.html`:

```liquid
{% include linkedin-feed.html posts_count="3" carousel="true" auto_refresh="true" %}
```

## 🔧 How It Works

1. **Fetches real LinkedIn posts** via RSS2JSON API
2. **Falls back to static data** if API unavailable
3. **Auto-refreshes** every 5 minutes
4. **Carousel display** with 3 posts
5. **Platform-agnostic** (works on GitHub Pages & Django)

## 📝 Configuration

Edit in `home.html`:
- `posts_count`: Number of posts to show (default: 3)
- `carousel`: Enable carousel mode (default: true)
- `auto_refresh`: Auto-refresh posts (default: true)

## 🎨 Styling

All styles in `linkedin-feed-compact.css` - compact, modern design optimized for top-of-page placement.

## 📊 Data Source

**Primary:** LinkedIn RSS via RSS2JSON API  
**Fallback:** `data/posts.json` (3 sample posts)

---

**Status:** ✅ Active & Deployed  
**Location:** Top of home page (after hero section)
