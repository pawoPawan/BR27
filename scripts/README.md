# BR27 Scripts

Utility scripts for managing the BR27 website.

## 📦 Available Scripts

### **Platform Migration**

`migrate-platform.py` - Switch between GitHub Pages and Django

```bash
# Check current platform
python scripts/migrate-platform.py --status

# Migrate to Django
python scripts/migrate-platform.py --to django

# Revert to GitHub Pages
python scripts/migrate-platform.py --to github
```

---

## 🎯 Platform Migration

### **From GitHub Pages to Django:**

```bash
# 1. Check status
python scripts/migrate-platform.py --status

# 2. Migrate
python scripts/migrate-platform.py --to django

# 3. Deploy Django backend
cd django
python manage.py collectstatic
# Deploy to Railway/Heroku/etc

# 4. Update DNS to point to new server
```

### **From Django back to GitHub Pages:**

```bash
python scripts/migrate-platform.py --to github
git push origin main
```

---

## 🔧 How It Works

The migration script:
1. Updates `config/platform.json`
2. Syncs templates between Jekyll and Django
3. Converts template syntax (Liquid ↔ Jinja2)
4. Updates routing configuration

---

## 📚 Documentation

- **Migration Guide**: `/MIGRATION_GUIDE.md`
- **Feeds Configuration**: `/FEEDS_CONFIGURATION.md`
- **Platform Config**: `/config/platform.json`

---

**All scripts are designed to make platform migration effortless!**

