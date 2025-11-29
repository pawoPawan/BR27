# Feeds Configuration System

## 🎯 Modular Feed Architecture

All social feeds (LinkedIn, Twitter, YouTube, etc.) are now modular and configurable without touching the main HTML files!

---

## 📦 Structure

```
_includes/
├── head-feeds.html           # CSS & JS includes
├── linkedin-feed.html        # LinkedIn feed component
├── feeds-loader.html         # Dynamic loader
└── (future: twitter-feed.html, youtube-feed.html)

_data/
└── feeds.yml                 # ✨ Configuration file

home.html                     # Just includes {% include feeds-loader.html %}
```

---

## ⚙️ How to Configure Feeds

### **Edit one file:** `_data/feeds.yml`

```yaml
home_page:
  feeds:
    - type: linkedin
      enabled: true          # Turn on/off
      posts_count: 3         # How many posts
      carousel: true         # Carousel mode
      auto_refresh: true     # Auto-refresh
      position: before_footer
```

---

## 🎯 Usage Examples

### **Enable/Disable LinkedIn Feed**

```yaml
# Turn OFF
enabled: false

# Turn ON
enabled: true
```

### **Change Number of Posts**

```yaml
posts_count: 3    # Show 3 posts
posts_count: 6    # Show 6 posts
posts_count: 10   # Show 10 posts
```

### **Toggle Carousel**

```yaml
carousel: true    # Rotating carousel
carousel: false   # Static grid
```

### **Change Position**

```yaml
position: before_footer   # Before footer section
position: after_impact    # After impact section
position: after_cta       # After CTA section
```

---

## 🔮 Add New Feeds (Future)

### **1. Create the Include**

Create `_includes/twitter-feed.html`:
```html
<section class="twitter-feed-section">
    <!-- Twitter feed HTML -->
</section>
```

### **2. Add to Configuration**

In `_data/feeds.yml`:
```yaml
home_page:
  feeds:
    - type: linkedin
      enabled: true
      posts_count: 3
    
    - type: twitter      # NEW!
      enabled: true
      tweets_count: 5
      position: after_impact
```

### **3. Update Loader**

In `_includes/feeds-loader.html`, add:
```liquid
{% when "twitter" %}
  {% include twitter-feed.html tweets_count=feed.tweets_count %}
```

**That's it!** No changes to home.html needed!

---

## 📝 Configuration for Different Pages

### **Home Page**
```yaml
home_page:
  feeds:
    - type: linkedin
      enabled: true
      posts_count: 3
      carousel: true
```

### **Articles Page**
```yaml
articles_page:
  feeds:
    - type: linkedin
      enabled: true
      posts_count: 20
      carousel: false
      grid: true
```

### **Focus Area Pages**
```yaml
focus_pages:
  feeds:
    - type: linkedin
      enabled: true
      posts_count: 3
      carousel: false
```

---

## 🚀 Benefits

✅ **No HTML Changes** - All configuration in one YAML file
✅ **Easy Enable/Disable** - Just change `enabled: true/false`
✅ **Reusable Components** - Write once, use everywhere
✅ **Future-Proof** - Easy to add Twitter, YouTube, etc.
✅ **Per-Page Control** - Different feeds on different pages
✅ **Clean Code** - Separation of concerns

---

## 🎯 Quick Actions

### **To Disable LinkedIn Feed:**
```yaml
# In _data/feeds.yml
enabled: false
```

### **To Change Post Count:**
```yaml
# In _data/feeds.yml
posts_count: 6
```

### **To Add on Another Page:**
```yaml
# In _data/feeds.yml
about_page:
  feeds:
    - type: linkedin
      enabled: true
      posts_count: 3
```

Then in `about.html`:
```liquid
{% include feeds-loader.html page_type="about_page" %}
```

---

## 📚 Files to Edit

**To Configure Feeds:**
- `_data/feeds.yml` ← Edit this!

**To Add New Feed Types:**
1. Create `_includes/{feed-name}-feed.html`
2. Update `_includes/feeds-loader.html`
3. Add to `_data/feeds.yml`

**Never Need to Touch:**
- `home.html` ✅
- `focus-areas/*.html` ✅
- Other page files ✅

---

## ✨ Example: Add YouTube Feed

**Step 1:** Create `_includes/youtube-feed.html`
**Step 2:** Add to `_data/feeds.yml`:
```yaml
home_page:
  feeds:
    - type: linkedin
      enabled: true
    - type: youtube
      enabled: true
      videos_count: 3
```
**Step 3:** Update `feeds-loader.html` with YouTube case

**Done!** YouTube feed appears automatically!

---

**All feed management is now centralized in `_data/feeds.yml`!** 🎉

