# BR27 Website

**Empowering minds. Enabling progress.**

A modern, responsive website for BR27 - a knowledge-driven initiative focused on empowering people through awareness, clarity, and practical insights.

## 🚀 Features

- **Modern Design**: Beautiful gradient-based UI with smooth animations
- **Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **Interactive Elements**: 
  - Smooth scrolling navigation
  - Animated statistics counters
  - Hover effects and transitions
  - Mobile-friendly hamburger menu
  - Parallax scrolling effects
  - Cursor trail effect (desktop only)
- **Performance Optimized**: Clean code with efficient animations
- **Accessibility**: Semantic HTML and ARIA labels

## 📁 Project Structure

```
br27/
├── index.html       # Main HTML file
├── styles.css       # CSS styling and animations
├── script.js        # JavaScript for interactivity
├── setup.sh         # Server management script
├── overview.txt     # Project overview
└── README.md        # This file
```

## 🎨 Sections

1. **Hero Section**: Eye-catching introduction with call-to-action buttons
2. **About Section**: Mission, approach, and vision cards
3. **Focus Areas**: Five key domains (Technology, Governance, Skills, Rural Development, Financial Awareness)
4. **Impact Section**: Animated statistics and visual cards
5. **CTA Section**: Call-to-action for engagement
6. **Footer**: Links, social media, and additional information

## 🛠️ Technologies Used

- HTML5
- CSS3 (with CSS Grid, Flexbox, and custom animations)
- Vanilla JavaScript (ES6+)
- Google Fonts (Inter & Poppins)

## 📱 How to Use

### Quick Start with setup.sh (Recommended)

The easiest way to manage the website is using the included `setup.sh` script:

```bash
# Start the web server
./setup.sh start

# Open website in browser (starts server if needed)
./setup.sh open

# Check if server is running
./setup.sh status

# Stop the server
./setup.sh stop

# Restart the server
./setup.sh restart

# View server logs
./setup.sh logs

# Show all available commands
./setup.sh help
```

### Manual Setup

1. **Open the website**: Simply open `index.html` in your web browser
   - Double-click the file, or
   - Right-click and select "Open with" your preferred browser

2. **For live development**: Use a local server manually
   ```bash
   # Using Python 3
   python3 -m http.server 8000
   
   # Using Node.js (if you have http-server installed)
   npx http-server
   ```
   Then visit `http://localhost:8000` in your browser

### Deployment

You can deploy this website to any static hosting service:

- **GitHub Pages**: Push to GitHub and enable Pages in repository settings
- **Netlify**: Drag and drop the folder to Netlify
- **Vercel**: Import the project and deploy
- **Cloudflare Pages**: Connect your repository and deploy
- **Any web hosting**: Upload files via FTP to your hosting provider

## 🎯 Customization

### Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --accent-color: #f093fb;
    /* ... more variables */
}
```

### Content
- Edit text content directly in `index.html`
- Modify focus areas, mission statements, and descriptions as needed

### Animations
- Adjust animation timings in `styles.css`
- Enable/disable effects in `script.js`

## 🌟 Key Focus Areas

1. **Technology** - Digital tools and emerging tech insights
2. **Governance** - Policy transparency and civic engagement
3. **Skills Development** - Practical training for modern careers
4. **Rural Development** - Sustainable growth pathways
5. **Financial Awareness** - Financial literacy and investment guidance

## 📞 Contact & Social

Update social media links in the footer section of `index.html` with your actual profiles.

## 📄 License

This project is created for BR27 initiative. Feel free to modify and use as needed.

## 🌐 Deployment

### Quick Deploy to GitHub Pages

```bash
# Automated deployment
./deploy-github.sh

# Or follow the detailed guide
```

See [QUICKSTART.md](QUICKSTART.md) for 5-minute deployment guide.

See [DEPLOYMENT.md](DEPLOYMENT.md) for:
- Detailed GitHub Pages setup
- Custom domain configuration (br27.in)
- AWS migration guide
- Security best practices

### Live URLs

- **Production**: [https://br27.in](https://br27.in)
- **GitHub Pages**: https://pawopawan.github.io/br27/
- **Repository**: [https://github.com/pawoPawan/br27](https://github.com/pawoPawan/br27)

## 🔄 Making Updates

After deploying, update your site:

```bash
# Make your changes, then:
./deploy-github.sh "Description of changes"

# Changes will be live in 1-5 minutes
```

## 🙏 Credits

- Fonts: Google Fonts (Inter, Poppins)
- Icons: Custom SVG icons
- Design: Custom modern gradient theme
- Hosting: GitHub Pages (moving to AWS)

---

**Building a confident, future-ready ecosystem — one idea at a time.**

🌐 Visit us: [https://br27.in](https://br27.in)

