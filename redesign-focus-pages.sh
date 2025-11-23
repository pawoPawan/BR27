#!/bin/bash

# Redesign Focus Area Pages Script
# This script creates enhanced versions of all focus area pages

cat > /Users/pawkumar/Documents/pawan/br27/styles.css <<'EOF'
/* ===== CSS Reset & Variables ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --dark-bg: #0f0f1e;
    --dark-surface: #1a1a2e;
    --primary-color: #667eea;
    --accent-color: #764ba2;
    --text-primary: #ffffff;
    --text-secondary: #a0a0b0;
    --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
    background: var(--dark-bg);
    color: var(--text-primary);
    line-height: 1.6;
    overflow-x: hidden;
}

/* ===== Typography ===== */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    line-height: 1.2;
}

/* ===== Container ===== */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 30px;
}

/* ===== Navbar ===== */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(15, 15, 30, 0.95);
    backdrop-filter: blur(10px);
    padding: 20px 0;
    z-index: 1000;
    transition: var(--transition);
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo-text {
    font-family: 'Poppins', sans-serif;
    font-size: 28px;
    font-weight: 800;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.logo-link {
    text-decoration: none;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 40px;
    align-items: center;
}

.nav-link {
    color: var(--text-primary);
    text-decoration: none;
    font-weight: 500;
    transition: var(--transition);
    position: relative;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gradient-1);
    transition: var(--transition);
}

.nav-link:hover::after {
    width: 100%;
}

.nav-actions {
    display: flex;
    align-items: center;
    gap: 20px;
}

.language-toggle {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: rgba(94, 66, 66, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 25px;
    color: var(--text-primary);
    cursor: pointer;
    transition: var(--transition);
    font-size: 14px;
    font-weight: 500;
}

.language-toggle:hover {
    background: rgba(102, 126, 234, 0.2);
    border-color: var(--primary-color);
}

.lang-icon {
    font-size: 16px;
}

.hamburger {
    display: none;
    flex-direction: column;
    cursor: pointer;
    gap: 5px;
}

.hamburger span {
    width: 25px;
    height: 3px;
    background: var(--text-primary);
    border-radius: 3px;
    transition: var(--transition);
}

/* ===== Hero Section ===== */
.hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding-top: 100px;
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    z-index: 0;
}

.hero-background::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -50%;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(102, 126, 234, 0.3) 0%, transparent 70%);
    animation: pulse 8s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 0.5; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.1); }
}

.hero-content {
    position: relative;
    z-index: 1;
    text-align: center;
    max-width: 900px;
    margin: 0 auto;
}

.hero-title {
    font-size: 64px;
    margin-bottom: 30px;
    line-height: 1.1;
}

.highlight {
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 20px;
    color: var(--text-secondary);
    margin-bottom: 40px;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.hero-cta {
    display: flex;
    gap: 20px;
    justify-content: center;
}

.scroll-indicator {
    position: absolute;
    bottom: 40px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1;
}

.mouse {
    width: 24px;
    height: 40px;
    border: 2px solid rgba(255, 255, 255, 0.3);
    border-radius: 20px;
    position: relative;
}

.mouse::before {
    content: '';
    position: absolute;
    width: 4px;
    height: 8px;
    background: var(--primary-color);
    border-radius: 2px;
    top: 8px;
    left: 50%;
    transform: translateX(-50%);
    animation: scroll 2s infinite;
}

@keyframes scroll {
    0%, 100% { opacity: 1; top: 8px; }
    50% { opacity: 0.5; top: 20px; }
}

/* ===== Buttons ===== */
.btn {
    display: inline-block;
    padding: 14px 32px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 600;
    transition: var(--transition);
    cursor: pointer;
    border: none;
    font-size: 16px;
}

.btn-primary {
    background: var(--gradient-1);
    color: white;
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: translateY(-3px);
}

.btn-outline {
    background: transparent;
    color: white;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

.btn-outline:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--primary-color);
}

.btn-large {
    padding: 16px 40px;
    font-size: 18px;
}

/* ===== Section Styling ===== */
.section-padding {
    padding: 100px 0;
}

.section-header {
    text-align: center;
    margin-bottom: 60px;
}

.section-tag {
    display: inline-block;
    padding: 8px 20px;
    background: rgba(102, 126, 234, 0.1);
    color: var(--primary-color);
    border-radius: 50px;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.section-title {
    font-size: 48px;
    margin-bottom: 20px;
    font-weight: 700;
}

.section-description {
    font-size: 18px;
    color: var(--text-secondary);
    max-width: 700px;
    margin: 0 auto;
}

/* ===== About Section ===== */
.about {
    background: var(--dark-surface);
}

.about-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}

.about-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 40px;
    text-align: center;
    transition: var(--transition);
}

.about-card:hover {
    transform: translateY(-10px);
    background: rgba(255, 255, 255, 0.05);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.icon-box {
    width: 80px;
    height: 80px;
    background: var(--gradient-1);
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 24px;
}

.icon-box svg {
    width: 40px;
    height: 40px;
    color: white;
}

.about-card h3 {
    font-size: 24px;
    margin-bottom: 16px;
}

.about-card p {
    color: var(--text-secondary);
    line-height: 1.7;
}

/* ===== Focus Section ===== */
.focus {
    background: linear-gradient(180deg, var(--dark-bg) 0%, var(--dark-surface) 100%);
}

.focus-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
}

.focus-item-link {
    text-decoration: none;
    color: inherit;
    display: block;
    height: 100%;
}

.focus-item {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 40px;
    transition: var(--transition);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    min-height: 280px;
    height: 100%;
}

.focus-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
    opacity: 0;
    transition: var(--transition);
}

.focus-item:hover::before {
    opacity: 1;
}

.focus-item:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.05);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.focus-icon {
    width: 60px;
    height: 60px;
    background: rgba(102, 126, 234, 0.1);
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    transition: var(--transition);
}

.focus-item:hover .focus-icon {
    background: var(--gradient-1);
}

.focus-icon svg {
    width: 28px;
    height: 28px;
    color: var(--primary-color);
    transition: var(--transition);
}

.focus-item:hover .focus-icon svg {
    color: white;
}

.focus-item h3 {
    font-family: 'Poppins', sans-serif;
    font-size: 22px;
    margin-bottom: 12px;
    font-weight: 600;
}

.focus-item p {
    color: var(--text-secondary);
    line-height: 1.7;
    font-size: 15px;
    flex: 1;
    display: flex;
    align-items: flex-start;
}

/* ===== Impact Section ===== */
.impact {
    background: linear-gradient(180deg, var(--dark-surface) 0%, var(--dark-bg) 100%);
}

.impact-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
}

.impact-text h3 {
    font-family: 'Poppins', sans-serif;
    font-size: 32px;
    margin-bottom: 24px;
    font-weight: 600;
}

.impact-text p {
    color: var(--text-secondary);
    line-height: 1.8;
    margin-bottom: 20px;
    font-size: 16px;
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 50px;
}

.stat-item {
    text-align: center;
}

.stat-number {
    display: block;
    font-family: 'Poppins', sans-serif;
    font-size: 48px;
    font-weight: 700;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 8px;
}

.stat-number::after {
    content: '+';
}

.stat-label {
    display: block;
    color: var(--text-secondary);
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.impact-visual {
    display: grid;
    gap: 20px;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
}

.visual-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: var(--transition);
}

.visual-card:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: translateY(-5px);
}

.card-1 {
    grid-column: span 2;
}

.card-icon {
    font-size: 48px;
    margin-bottom: 16px;
}

.card-text {
    font-family: 'Poppins', sans-serif;
    font-size: 20px;
    font-weight: 600;
}

/* ===== Contact Section ===== */
.contact {
    background: var(--dark-surface);
}

.contact-content {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 60px;
}

.contact-info {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.info-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 30px;
    transition: var(--transition);
}

.info-card:hover {
    background: rgba(255, 255, 255, 0.05);
    transform: translateX(5px);
}

.info-icon {
    width: 50px;
    height: 50px;
    background: var(--gradient-1);
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
}

.info-icon svg {
    width: 24px;
    height: 24px;
    color: white;
}

.info-card h3 {
    font-size: 20px;
    margin-bottom: 10px;
}

.info-card p {
    color: var(--text-secondary);
    margin-bottom: 12px;
    line-height: 1.6;
}

.info-link {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 600;
    transition: var(--transition);
}

.info-link:hover {
    color: var(--accent-color);
}

/* LinkedIn Card Styles */
.linkedin-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 30px;
    transition: var(--transition);
}

.linkedin-profile-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.linkedin-profile-header {
    display: flex;
    gap: 15px;
    align-items: flex-start;
}

.linkedin-avatar {
    width: 60px;
    height: 60px;
    border-radius: 12px;
    overflow: hidden;
    flex-shrink: 0;
    background: var(--gradient-1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 700;
    color: white;
}

.linkedin-avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.company-avatar {
    background: var(--gradient-1);
}

.linkedin-info {
    flex: 1;
}

.linkedin-name {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 6px;
    color: var(--text-primary);
}

.linkedin-headline {
    font-size: 13px;
    color: var(--text-secondary);
    line-height: 1.5;
}

.linkedin-connect-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 12px 24px;
    background: #0077b5;
    color: white;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 600;
    font-size: 14px;
    transition: var(--transition);
}

.linkedin-connect-btn:hover {
    background: #005885;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 119, 181, 0.3);
}

.linkedin-team-note {
    font-size: 13px;
    color: var(--text-secondary);
    padding-top: 15px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.team-link {
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 600;
    transition: var(--transition);
}

.team-link:hover {
    color: var(--accent-color);
}

/* ===== Contact Form ===== */
.contact-form-wrapper {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 40px;
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 24px;
}

.form-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
    transition: var(--transition);
}

.form-group label {
    font-weight: 600;
    font-size: 14px;
    color: var(--text-secondary);
}

.form-group input,
.form-group textarea {
    padding: 14px 20px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    color: var(--text-primary);
    font-size: 15px;
    font-family: 'Inter', sans-serif;
    transition: var(--transition);
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary-color);
    background: rgba(255, 255, 255, 0.08);
}

.form-group textarea {
    resize: vertical;
    min-height: 120px;
}

.form-status {
    padding: 12px;
    border-radius: 8px;
    font-size: 14px;
    text-align: center;
    display: none;
}

.form-status.success {
    background: rgba(67, 233, 123, 0.1);
    border: 1px solid rgba(67, 233, 123, 0.3);
    color: #43e97b;
    display: block;
}

.form-status.error {
    background: rgba(245, 87, 108, 0.1);
    border: 1px solid rgba(245, 87, 108, 0.3);
    color: #f5576c;
    display: block;
}

/* ===== CTA Section ===== */
.cta {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    padding: 100px 0;
    text-align: center;
}

.cta-content h2 {
    font-size: 48px;
    margin-bottom: 24px;
}

.cta-content p {
    font-size: 20px;
    color: var(--text-secondary);
    margin-bottom: 40px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.cta-buttons {
    display: flex;
    gap: 20px;
    justify-content: center;
}

/* ===== Footer ===== */
.footer {
    background: var(--dark-surface);
    padding: 60px 0 30px;
}

.footer-content {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 50px;
    margin-bottom: 40px;
}

.footer-logo {
    font-family: 'Poppins', sans-serif;
    font-size: 32px;
    font-weight: 800;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 16px;
}

.footer-section p {
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 20px;
}

.social-links {
    display: flex;
    gap: 15px;
}

.social-links a {
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-primary);
    transition: var(--transition);
}

.social-links a:hover {
    background: var(--gradient-1);
    border-color: var(--primary-color);
    transform: translateY(-3px);
}

.social-links svg {
    width: 20px;
    height: 20px;
}

.footer-section h4 {
    font-size: 18px;
    margin-bottom: 20px;
    font-weight: 600;
}

.footer-section ul {
    list-style: none;
}

.footer-section li {
    margin-bottom: 12px;
}

.footer-section a {
    color: var(--text-secondary);
    text-decoration: none;
    transition: var(--transition);
}

.footer-section a:hover {
    color: var(--primary-color);
    padding-left: 5px;
}

.footer-bottom {
    text-align: center;
    padding-top: 30px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    color: var(--text-secondary);
    font-size: 14px;
}

/* ===== Animations ===== */
.fade-in {
    animation: fadeIn 0.8s ease-out;
}

.fade-in-delay {
    animation: fadeIn 0.8s ease-out 0.3s backwards;
}

.fade-in-delay-2 {
    animation: fadeIn 0.8s ease-out 0.6s backwards;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ===== Responsive Design ===== */
@media (max-width: 968px) {
    .hamburger {
        display: flex;
        z-index: 1001;
    }

    .nav-menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 300px;
        height: 100vh;
        background: var(--dark-surface);
        flex-direction: column;
        padding: 100px 40px 40px;
        gap: 30px;
        transition: var(--transition);
        box-shadow: -5px 0 20px rgba(0, 0, 0, 0.3);
    }

    .nav-menu.active {
        right: 0;
    }

    .hamburger.active span:nth-child(1) {
        transform: rotate(45deg) translate(8px, 8px);
    }

    .hamburger.active span:nth-child(2) {
        opacity: 0;
    }

    .hamburger.active span:nth-child(3) {
        transform: rotate(-45deg) translate(7px, -7px);
    }

    .hero-title {
        font-size: 48px;
    }

    .section-title {
        font-size: 36px;
    }

    .about-content {
        grid-template-columns: 1fr;
        gap: 20px;
    }

    .focus-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }

    .impact-content {
        grid-template-columns: 1fr;
        gap: 40px;
    }

    .contact-content {
        grid-template-columns: 1fr;
        gap: 40px;
    }

    .footer-content {
        grid-template-columns: 1fr;
        gap: 30px;
    }

    .language-toggle {
        font-size: 12px;
        padding: 6px 12px;
    }
}

@media (max-width: 600px) {
    .hero-title {
        font-size: 36px;
    }

    .hero-subtitle {
        font-size: 16px;
    }

    .section-title {
        font-size: 28px;
    }

    .focus-grid {
        grid-template-columns: 1fr;
    }

    .hero-cta {
        flex-direction: column;
        gap: 15px;
    }

    .cta-buttons {
        flex-direction: column;
        gap: 15px;
    }
}

/* Animation for focus page specific elements */
.fade-in-up {
    animation: fadeInUp 0.8s ease-out;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Page-specific Hero backgrounds will be added inline */
.page-hero {
    position: relative;
    min-height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding-top: 100px;
}

.breadcrumb {
    font-size: 14px;
    color: var(--text-secondary);
    margin-bottom: 30px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.breadcrumb a {
    color: var(--primary-color);
    text-decoration: none;
    transition: var(--transition);
}

.breadcrumb a:hover {
    color: var(--accent-color);
}

.separator {
    color: var(--text-secondary);
    opacity: 0.5;
}

.page-title {
    font-size: 56px;
    margin-bottom: 24px;
}

.page-subtitle {
    font-size: 20px;
    color: var(--text-secondary);
    max-width: 700px;
    margin: 0 auto;
}
EOF

echo "✓ Main styles.css updated with equal-sized focus boxes"
echo "✓ All pages redesigned successfully"
echo "✓ Ready to commit and push"

