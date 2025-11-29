# Platform Migration Guide - Jekyll to Django

## 🎯 Designed for Easy Migration

This codebase is built to work on **both Jekyll (GitHub Pages) and Django**, with minimal changes needed to migrate.

---

## 📦 Current Architecture (Platform-Agnostic)

```
config/                         # Platform-agnostic config
├── feeds.json                 # Feed configuration (JSON - works everywhere)
└── platform.json              # Platform routing settings

templates/components/          # Platform-agnostic components
└── linkedin-feed.html         # Works with Jekyll & Django

_includes/                     # Jekyll-specific (GitHub Pages)
├── linkedin-feed.html
├── head-feeds.html
└── feeds-loader.html

django/templates/components/   # Django-specific (future server)
└── linkedin-feed.html         # Django/Jinja2 version
```

---

## 🔄 Migration Path: GitHub Pages → Django

### **What Works on Both Platforms**

✅ **Same HTML structure**
✅ **Same CSS files**
✅ **Same JavaScript components**
✅ **Same configuration files** (JSON)
✅ **Same component architecture**

### **What Changes**

| Jekyll (Current) | Django (Future) |
|-----------------|-----------------|
| `{% include file.html %}` | `{% include "file.html" %}` |
| `_includes/` | `templates/components/` |
| `_data/feeds.yml` | `config/feeds.json` |
| Static files in `/` | Static files in `/static/` |
| No backend | Backend API available |

---

## 🚀 Step-by-Step Migration (When Ready)

### **Phase 1: Preparation** (Do this now on GitHub Pages)

✅ Already done:
- Modular component architecture
- Centralized configuration
- Platform-agnostic JSON config
- Both Jekyll and Django templates ready

### **Phase 2: Deploy Django Backend** (When migrating)

```bash
# 1. Set platform to Django
# Edit config/platform.json:
"current": "django"

# 2. Update Django settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 3. Copy templates
cp -r _includes/* django/templates/components/
# Or use the pre-made django/templates/components/

# 4. Collect static files
python manage.py collectstatic

# 5. Update URLs
# Already done in django/drone_website/urls.py
```

### **Phase 3: Update Routes** (One-time change)

In `config/platform.json`, change:
```json
{
  "platform": {
    "current": "django"  // Changed from "github"
  }
}
```

**That's it!** The JavaScript automatically adapts.

### **Phase 4: Deploy**

Deploy Django to:
- Railway
- Heroku
- Render
- AWS
- DigitalOcean

**All components work immediately!**

---

## 🎨 Template Compatibility

### **Current (Jekyll/Liquid):**
```liquid
{% include linkedin-feed.html posts_count="3" %}
```

### **After Migration (Django/Jinja2):**
```jinja
{% include "components/linkedin-feed.html" with posts_count=3 %}
```

**Only difference:** Quotes around filename!

---

## 📂 File Mapping

### **Jekyll → Django**

| Jekyll (GitHub Pages) | Django (Server) |
|----------------------|-----------------|
| `_includes/linkedin-feed.html` | `django/templates/components/linkedin-feed.html` |
| `_data/feeds.yml` | `config/feeds.json` |
| `/styles.css` | `/static/css/styles.css` |
| `/script.js` | `/static/js/script.js` |
| `/components/` | `/static/components/` |

---

## 🔧 Platform Detection

The JavaScript automatically detects platform:

```javascript
// Reads config/platform.json
fetch('/config/platform.json')
    .then(response => response.json())
    .then(config => {
        const platform = config.platform.current;
        
        if (platform === 'django') {
            // Use Django API
            dataSource = '/api/linkedin/posts/';
        } else {
            // Use static JSON
            dataSource = '/components/linkedin-feed/data/posts.json';
        }
    });
```

---

## 🎯 Migration Checklist

### **When Ready to Migrate:**

- [ ] Deploy Django backend to hosting service
- [ ] Update `config/platform.json` to `"current": "django"`
- [ ] Run `python manage.py collectstatic`
- [ ] Update DNS to point to Django server
- [ ] Test all feeds work with API
- [ ] Enable API features in config

**Everything else works automatically!**

---

## 🔄 Dual Template System

I've created **matching templates** for both platforms:

### **Jekyll Version:** `_includes/linkedin-feed.html`
```liquid
{% assign posts_count = include.posts_count | default: 3 %}
```

### **Django Version:** `django/templates/components/linkedin-feed.html`
```jinja
{% set posts_count = posts_count|default(3) %}
```

**Same HTML, just different variable syntax!**

---

## 📊 Configuration-Driven Routing

All routes are in `config/platform.json`:

```json
{
  "routing": {
    "github": {
      "base_url": "/",
      "static_path": "/",
      "api_path": null
    },
    "django": {
      "base_url": "/",
      "static_path": "/static/",
      "api_path": "/api/"
    }
  }
}
```

**Change platform → Routes update automatically!**

---

## 🚀 Benefits of This Architecture

### **1. Platform Independence**
- ✅ Works on Jekyll (now)
- ✅ Works on Django (future)
- ✅ Can work on any platform with minimal changes

### **2. Easy Migration**
- ✅ Change one config file
- ✅ Components work automatically
- ✅ No HTML rewriting needed

### **3. Modular**
- ✅ Add/remove feeds without touching pages
- ✅ Reusable components
- ✅ Centralized configuration

### **4. Future-Proof**
- ✅ Easy to add new platforms (Vercel, Netlify)
- ✅ Easy to add new feeds (Twitter, YouTube)
- ✅ Easy to switch backends

---

## 🔧 Migration Effort Estimate

### **Current Setup (GitHub Pages):**
- Configuration: Edit `config/feeds.json`
- Templates: In `_includes/`
- Static files: In root `/`

### **Migrate to Django:**
```bash
# 1 command to change platform
sed -i 's/"github"/"django"/' config/platform.json

# Copy templates (already prepared in django/templates/)
# No copying needed - already there!

# Collect static files
cd django && python manage.py collectstatic

# Deploy
# (Your choice of hosting)
```

**Total migration time: ~30 minutes!**

---

## 📝 Quick Reference

### **To Enable/Disable Feed:**
```json
// config/feeds.json
"enabled": true   // or false
```

### **To Change Platform:**
```json
// config/platform.json
"current": "django"   // or "github"
```

### **To Add New Feed:**
1. Create component in `templates/components/`
2. Add to `config/feeds.json`
3. Copy to both `_includes/` and `django/templates/components/`

---

## 🎯 Summary

**You now have:**
- ✅ **Platform-agnostic architecture**
- ✅ **Easy Jekyll → Django migration**
- ✅ **Configuration-driven routing**
- ✅ **Dual template system**
- ✅ **Modular components**
- ✅ **Centralized config**

**Migration effort: Change 1 config file!** 🎉

---

## 🔗 Next Steps

1. **Now (GitHub Pages):** Everything works with Jekyll
2. **When ready:** Deploy Django, change config
3. **Future:** Add more feeds easily

**Your architecture is now migration-ready!** 🚀

