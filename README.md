# BR27 - Empowering Minds. Enabling Progress.

Knowledge-driven initiative bridging the gap between potential and opportunity through actionable insights in technology, governance, skills, and beyond.

## 🌐 Live Site
**https://www.br27.in**

## 🏗️ Architecture

**Frontend:** Static HTML/CSS/JavaScript  
**Hosting:** GitHub Pages (Jekyll)  
**Backend:** Django (ready for future migration)  

### Platform-Agnostic Design
- Works on GitHub Pages (current)
- Ready for Django migration (future)
- One-command platform switching

## 📁 Structure

```
br27/
├── home.html                    # Main page
├── styles.css                   # Global styles
├── script.js                    # Main JavaScript
├── components/
│   └── linkedin-feed/          # LinkedIn feed module
│       ├── linkedin-feed-client.js
│       ├── linkedin-feed-compact.css
│       └── data/posts.json
├── _includes/                   # Jekyll includes
│   ├── linkedin-feed.html
│   └── head-feeds.html
├── config/
│   └── platform.json           # Platform configuration
├── django/                      # Django backend (future)
└── scripts/
    └── migrate-platform.py     # Platform migration tool
```

## 🚀 Features

- ✅ **Dynamic LinkedIn Feed** - Real posts via RSS2JSON API
- ✅ **Bilingual** - English & Hindi
- ✅ **Responsive Design** - Mobile-first approach
- ✅ **Modern UI/UX** - Gradient design, animations
- ✅ **Platform-Agnostic** - Easy migration path

## 🔄 Platform Migration

```bash
# Check current platform
python scripts/migrate-platform.py --status

# Migrate to Django (when ready)
python scripts/migrate-platform.py --to django
```

## 📚 Documentation

- **Migration Guide:** `MIGRATION_GUIDE.md`
- **Architecture:** `ARCHITECTURE.md`
- **Quick Start:** `QUICK_START.md`

## 🛠️ Development

### GitHub Pages (Current)
```bash
# Make changes and push
git add .
git commit -m "Your changes"
git push origin main
# GitHub Pages auto-deploys in 2-3 minutes
```

### Django (Future)
```bash
cd django
python manage.py runserver
```

## 📊 Technology Stack

**Current (GitHub Pages):**
- Jekyll (Liquid templates)
- Vanilla JavaScript
- CSS3 with CSS Variables
- RSS2JSON API

**Future (Django):**
- Django 5.0+
- Django REST Framework
- PostgreSQL
- Jinja2 templates

## 🎯 Focus Areas

- Technology & Innovation
- Governance & Policy
- Skills Development
- Rural Development
- Financial Awareness
- Education & Careers

## 📞 Contact

**Website:** https://www.br27.in  
**LinkedIn:** https://www.linkedin.com/company/27br/  
**YouTube:** https://www.youtube.com/@पल-दो-पल

---

**© 2025 BR27. All rights reserved.**  
Building a confident, future-ready ecosystem.
