// ===== Language Translation System =====
const translations = {
    en: {
        nav: { home: "Home", about: "About", focus: "Focus Areas", impact: "Impact", contact: "Contact" },
        hero: {
            title1: "Empowering Minds.",
            title2: "Enabling Progress.",
            subtitle: "A knowledge-driven initiative bridging the gap between potential and opportunity through actionable insights in technology, governance, skills, and beyond.",
            btn1: "Discover More",
            btn2: "Our Focus"
        },
        about: {
            tag: "Who We Are",
            title: "Building a Future-Ready Ecosystem",
            mission: {
                title: "Our Mission",
                text: "We believe real transformation begins with an informed society. BR27 bridges the gap between potential and opportunity by sharing actionable knowledge that empowers communities."
            },
            approach: {
                title: "Our Approach",
                text: "We create content, perspectives, and conversations that help individuals think deeper, grow faster, and make better choices for themselves and their communities."
            },
            vision: {
                title: "Our Vision",
                text: "Building a confident, future-ready ecosystem — one idea at a time. We empower minds through awareness, clarity, and practical insights."
            }
        },
        focus: {
            tag: "What We Do",
            title: "Our Focus Areas",
            description: "Actionable knowledge across domains for holistic development",
            tech: { title: "Technology", text: "Demystifying digital tools and emerging tech to help communities stay ahead in an ever-evolving landscape." },
            gov: { title: "Governance", text: "Bringing transparency and understanding to policies, rights, and civic engagement for informed participation." },
            skills: { title: "Skills Development", text: "Practical training and insights to build competencies that matter in today's job market and entrepreneurship." },
            rural: { title: "Rural Development", text: "Empowering rural communities with knowledge, resources, and pathways to sustainable growth and prosperity." },
            finance: { title: "Financial Awareness", text: "Building financial literacy from basics to smart investments, helping people make confident money decisions." },
            edu: { title: "Education Paths & Careers", text: "Guiding students through educational choices, career opportunities, and pathways to success in their chosen fields." }
        },
        impact: {
            tag: "Making a Difference",
            title: "One Idea at a Time",
            heading: "Real Transformation Through Knowledge",
            text1: "This is the first step toward building a confident, future-ready ecosystem. We believe that when people have access to the right information at the right time, they can make choices that transform not just their own lives, but their entire communities.",
            text2: "BR27 is more than an initiative — it's a movement toward creating an informed, empowered society where everyone has the tools to succeed.",
            card1: "Actionable Insights",
            card2: "Focused Content",
            card3: "Future Ready"
        },
        contact: {
            tag: "Get In Touch",
            title: "Contact Us",
            description: "Have questions or want to collaborate? We'd love to hear from you!",
            location: { title: "Location", text: "Working remotely to empower communities across India" },
            linkedin: { follow: "Follow on LinkedIn", team: "Meet our team:" },
            youtube: { title: "YouTube", text: "Watch our content and join the conversation", link: "Visit Channel" }
        },
        form: {
            name: { label: "Name", placeholder: "Your full name" },
            email: { label: "Email", placeholder: "your.email@example.com" },
            subject: { label: "Subject", placeholder: "What's this about?" },
            message: { label: "Message", placeholder: "Tell us more..." },
            submit: "Send Message"
        },
        cta: {
            title: "Ready to Empower Your Mind?",
            text: "Join us in building a future-ready ecosystem where knowledge meets opportunity.",
            btn1: "Get Started",
            btn2: "Learn More"
        },
        footer: {
            tagline: "Empowering minds. Enabling progress.",
            quicklinks: "Quick Links",
            focusareas: "Focus Areas",
            educareer: "Education & Careers",
            connect: "Connect",
            contactus: "Contact Us",
            learnmore: "Learn More",
            copyright: "© 2025 BR27. All rights reserved. Building a confident, future-ready ecosystem."
        }
    },
    hi: {
        nav: { home: "होम", about: "हमारे बारे में", focus: "फोकस क्षेत्र", impact: "प्रभाव", contact: "संपर्क करें" },
        hero: {
            title1: "मन को सशक्त बनाना।",
            title2: "प्रगति को सक्षम बनाना।",
            subtitle: "एक ज्ञान-संचालित पहल जो प्रौद्योगिकी, शासन, कौशल और अन्य क्षेत्रों में कार्रवाई योग्य अंतर्दृष्टि के माध्यम से क्षमता और अवसर के बीच की खाई को पाटती है।",
            btn1: "और जानें",
            btn2: "हमारा फोकस"
        },
        about: {
            tag: "हम कौन हैं",
            title: "भविष्य के लिए तैयार पारिस्थितिकी तंत्र का निर्माण",
            mission: {
                title: "हमारा मिशन",
                text: "हम मानते हैं कि वास्तविक परिवर्तन एक सूचित समाज से शुरू होता है। BR27 कार्रवाई योग्य ज्ञान साझा करके क्षमता और अवसर के बीच की खाई को पाटता है जो समुदायों को सशक्त बनाता है।"
            },
            approach: {
                title: "हमारा दृष्टिकोण",
                text: "हम ऐसी सामग्री, दृष्टिकोण और बातचीत बनाते हैं जो व्यक्तियों को गहराई से सोचने, तेजी से बढ़ने और अपने और अपने समुदायों के लिए बेहतर विकल्प चुनने में मदद करती है।"
            },
            vision: {
                title: "हमारी दृष्टि",
                text: "एक आत्मविश्वासी, भविष्य के लिए तैयार पारिस्थितिकी तंत्र का निर्माण — एक समय में एक विचार। हम जागरूकता, स्पष्टता और व्यावहारिक अंतर्दृष्टि के माध्यम से मन को सशक्त बनाते हैं।"
            }
        },
        focus: {
            tag: "हम क्या करते हैं",
            title: "हमारे फोकस क्षेत्र",
            description: "समग्र विकास के लिए विभिन्न क्षेत्रों में कार्रवाई योग्य ज्ञान",
            tech: { title: "प्रौद्योगिकी", text: "डिजिटल टूल और उभरती तकनीक को सरल बनाना ताकि समुदाय लगातार बदलते परिदृश्य में आगे रह सकें।" },
            gov: { title: "शासन", text: "नीतियों, अधिकारों और नागरिक भागीदारी में पारदर्शिता और समझ लाना ताकि सूचित भागीदारी हो सके।" },
            skills: { title: "कौशल विकास", text: "व्यावहारिक प्रशिक्षण और अंतर्दृष्टि जो आज के नौकरी बाजार और उद्यमिता में मायने रखने वाली दक्षताओं का निर्माण करती है।" },
            rural: { title: "ग्रामीण विकास", text: "ग्रामीण समुदायों को ज्ञान, संसाधन और टिकाऊ विकास और समृद्धि के मार्गों के साथ सशक्त बनाना।" },
            finance: { title: "वित्तीय जागरूकता", text: "बुनियादी बातों से लेकर स्मार्ट निवेश तक वित्तीय साक्षरता का निर्माण, लोगों को आत्मविश्वास से पैसे के फैसले लेने में मदद करना।" },
            edu: { title: "शिक्षा पथ और करियर", text: "छात्रों को शैक्षिक विकल्पों, करियर के अवसरों और उनके चुने हुए क्षेत्रों में सफलता के मार्गों के माध्यम से मार्गदर्शन करना।" }
        },
        impact: {
            tag: "बदलाव लाना",
            title: "एक समय में एक विचार",
            heading: "ज्ञान के माध्यम से वास्तविक परिवर्तन",
            text1: "यह एक आत्मविश्वासी, भविष्य के लिए तैयार पारिस्थितिकी तंत्र के निर्माण की दिशा में पहला कदम है। हम मानते हैं कि जब लोगों को सही समय पर सही जानकारी मिलती है, तो वे ऐसे विकल्प चुन सकते हैं जो न केवल उनके अपने जीवन को बदलते हैं, बल्कि उनके पूरे समुदायों को भी बदलते हैं।",
            text2: "BR27 सिर्फ एक पहल से अधिक है — यह एक सूचित, सशक्त समाज बनाने की दिशा में एक आंदोलन है जहां सभी के पास सफल होने के उपकरण हैं।",
            card1: "कार्रवाई योग्य अंतर्दृष्टि",
            card2: "केंद्रित सामग्री",
            card3: "भविष्य के लिए तैयार"
        },
        contact: {
            tag: "संपर्क में रहें",
            title: "हमसे संपर्क करें",
            description: "क्या आपके कोई प्रश्न हैं या सहयोग करना चाहते हैं? हम आपसे सुनना पसंद करेंगे!",
            location: { title: "स्थान", text: "भारत भर में समुदायों को सशक्त बनाने के लिए दूरस्थ रूप से काम कर रहे हैं" },
            linkedin: { follow: "LinkedIn पर फॉलो करें", team: "हमारी टीम से मिलें:" },
            youtube: { title: "YouTube", text: "हमारी सामग्री देखें और बातचीत में शामिल हों", link: "चैनल पर जाएं" }
        },
        form: {
            name: { label: "नाम", placeholder: "आपका पूरा नाम" },
            email: { label: "ईमेल", placeholder: "आपका.ईमेल@example.com" },
            subject: { label: "विषय", placeholder: "यह किस बारे में है?" },
            message: { label: "संदेश", placeholder: "हमें और बताएं..." },
            submit: "संदेश भेजें"
        },
        cta: {
            title: "अपने दिमाग को सशक्त बनाने के लिए तैयार हैं?",
            text: "एक भविष्य के लिए तैयार पारिस्थितिकी तंत्र बनाने में हमारे साथ शामिल हों जहां ज्ञान अवसर से मिलता है।",
            btn1: "शुरू करें",
            btn2: "और जानें"
        },
        footer: {
            tagline: "मन को सशक्त बनाना। प्रगति को सक्षम बनाना।",
            quicklinks: "त्वरित लिंक",
            focusareas: "फोकस क्षेत्र",
            educareer: "शिक्षा और करियर",
            connect: "जुड़ें",
            contactus: "संपर्क करें",
            learnmore: "और जानें",
            copyright: "© 2025 BR27. सर्वाधिकार सुरक्षित। एक आत्मविश्वासी, भविष्य के लिए तैयार पारिस्थितिकी तंत्र का निर्माण।"
        }
    }
};

let currentLanguage = localStorage.getItem('br27-language') || 'en';

function applyTranslations(lang) {
    currentLanguage = lang;
    localStorage.setItem('br27-language', lang);
    document.documentElement.lang = lang;
    
    document.querySelectorAll('[data-translate]').forEach(element => {
        const key = element.getAttribute('data-translate');
        const keys = key.split('.');
        let translation = translations[lang];
        for (const k of keys) translation = translation?.[k];
        if (translation) element.textContent = translation;
    });
    
    document.querySelectorAll('[data-translate-placeholder]').forEach(element => {
        const key = element.getAttribute('data-translate-placeholder');
        const keys = key.split('.');
        let translation = translations[lang];
        for (const k of keys) translation = translation?.[k];
        if (translation) element.placeholder = translation;
    });
    
    const langText = document.getElementById('langText');
    if (langText) langText.textContent = lang === 'en' ? 'हिंदी' : 'English';
}

// Apply saved language on page load
document.addEventListener('DOMContentLoaded', function() {
    applyTranslations(currentLanguage);
    
    const languageToggle = document.getElementById('languageToggle');
    if (languageToggle) {
        languageToggle.addEventListener('click', function() {
            applyTranslations(currentLanguage === 'en' ? 'hi' : 'en');
        });
    }
});

// ===== Mobile Navigation Toggle =====
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close menu when clicking on a link
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// ===== Smooth Scroll with Offset =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offset = 80; // navbar height
            const targetPosition = target.offsetTop - offset;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ===== Navbar Background on Scroll =====
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
        navbar.style.background = 'rgba(15, 15, 30, 0.98)';
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
    } else {
        navbar.style.background = 'rgba(15, 15, 30, 0.95)';
        navbar.style.boxShadow = 'none';
    }
    
    lastScroll = currentScroll;
});

// ===== Intersection Observer for Fade-In Animations =====
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards and items
document.querySelectorAll('.about-card, .focus-item, .visual-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
});

// ===== Animated Counter for Stats =====
const animateCounter = (element, target, duration) => {
    let start = 0;
    const increment = target / (duration / 16); // 60 FPS
    
    const updateCounter = () => {
        start += increment;
        if (start < target) {
            element.textContent = Math.ceil(start);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    };
    
    updateCounter();
};

// Trigger counter animation when stats section is visible
const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
            entry.target.classList.add('animated');
            const statNumbers = entry.target.querySelectorAll('.stat-number');
            statNumbers.forEach(stat => {
                const target = parseInt(stat.getAttribute('data-target'));
                animateCounter(stat, target, 2000);
            });
        }
    });
}, { threshold: 0.5 });

const statsGrid = document.querySelector('.stats-grid');
if (statsGrid) {
    statsObserver.observe(statsGrid);
}

// ===== Parallax Effect on Hero =====
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const heroBackground = document.querySelector('.hero-background');
    if (heroBackground) {
        heroBackground.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// ===== Dynamic Focus Item Colors =====
document.querySelectorAll('.focus-item').forEach((item, index) => {
    const colors = [
        'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
        'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
        'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
        'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'
    ];
    
    const color = colors[index % colors.length];
    
    item.addEventListener('mouseenter', () => {
        item.style.borderImage = color + ' 1';
        item.style.borderImageSlice = '1';
    });
    
    item.addEventListener('mouseleave', () => {
        item.style.borderImage = 'none';
    });
});

// ===== Cursor Trail Effect (Desktop Only) =====
if (window.innerWidth > 768) {
    const coords = { x: 0, y: 0 };
    const circles = document.querySelectorAll('.cursor-circle');
    
    // Create cursor circles
    if (circles.length === 0) {
        for (let i = 0; i < 20; i++) {
            const circle = document.createElement('div');
            circle.className = 'cursor-circle';
            circle.style.cssText = `
                position: fixed;
                width: 10px;
                height: 10px;
                border-radius: 50%;
                background: rgba(102, 126, 234, 0.1);
                pointer-events: none;
                z-index: 9999;
                transition: transform 0.1s;
            `;
            document.body.appendChild(circle);
        }
    }
    
    const circles2 = document.querySelectorAll('.cursor-circle');
    
    circles2.forEach((circle, index) => {
        circle.x = 0;
        circle.y = 0;
    });
    
    window.addEventListener('mousemove', (e) => {
        coords.x = e.clientX;
        coords.y = e.clientY;
    });
    
    const animateCircles = () => {
        let x = coords.x;
        let y = coords.y;
        
        circles2.forEach((circle, index) => {
            circle.style.left = x - 5 + 'px';
            circle.style.top = y - 5 + 'px';
            circle.style.transform = `scale(${(circles2.length - index) / circles2.length})`;
            
            circle.x = x;
            circle.y = y;
            
            const nextCircle = circles2[index + 1] || circles2[0];
            x += (nextCircle.x - x) * 0.3;
            y += (nextCircle.y - y) * 0.3;
        });
        
        requestAnimationFrame(animateCircles);
    };
    
    animateCircles();
}

// ===== Active Nav Link on Scroll =====
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link');

const highlightNav = () => {
    const scrollY = window.pageYOffset;
    
    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.style.color = '';
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.style.color = '#667eea';
                }
            });
        }
    });
};

window.addEventListener('scroll', highlightNav);

// ===== Preloader (Optional) =====
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
});

// ===== Add hover effects to buttons =====
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('mouseenter', function(e) {
        const x = e.pageX - this.offsetLeft;
        const y = e.pageY - this.offsetTop;
        
        const ripple = document.createElement('span');
        ripple.style.cssText = `
            position: absolute;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            transform: translate(-50%, -50%);
            left: ${x}px;
            top: ${y}px;
            animation: ripple 0.6s ease-out;
        `;
        
        this.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// Add ripple animation
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            width: 300px;
            height: 300px;
            opacity: 0;
        }
    }
    .btn {
        position: relative;
        overflow: hidden;
    }
`;
document.head.appendChild(style);

// ===== Contact Form Handling with Formspree =====
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const submitBtn = contactForm.querySelector('button[type="submit"]');
        const formStatus = document.getElementById('form-status');
        const originalText = submitBtn.textContent;
        
        // Show loading state
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;
        formStatus.textContent = '';
        
        try {
            // Get form data
            const formData = new FormData(contactForm);
            
            // Send to Formspree
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (response.ok) {
                // Success
                submitBtn.textContent = '✓ Message Sent!';
                submitBtn.style.background = 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)';
                formStatus.textContent = 'Thank you! Your message has been sent successfully.';
                formStatus.className = 'form-status success';
                
                // Reset form
                contactForm.reset();
                
                // Reset button after delay
                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.style.background = '';
                    submitBtn.disabled = false;
                    formStatus.textContent = '';
                }, 5000);
            } else {
                throw new Error('Form submission failed');
            }
        } catch (error) {
            // Error handling
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            formStatus.textContent = 'Oops! There was a problem sending your message. Please try again.';
            formStatus.className = 'form-status error';
            
            setTimeout(() => {
                formStatus.textContent = '';
            }, 5000);
        }
    });
    
    // Add input animations
    const inputs = contactForm.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.style.transform = 'translateX(5px)';
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.style.transform = 'translateX(0)';
        });
    });
}

// ===== Console Message =====
console.log('%cBR27', 'font-size: 48px; font-weight: bold; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;');
console.log('%cEmpowering minds. Enabling progress.', 'font-size: 16px; color: #667eea;');
console.log('%c🚀 Building a confident, future-ready ecosystem — one idea at a time.', 'font-size: 14px; color: #a0a0b0;');
console.log('%c💼 LinkedIn: https://www.linkedin.com/company/27br/', 'font-size: 12px; color: #a0a0b0;');
console.log('%c📺 YouTube: https://www.youtube.com/@पल-दो-पल', 'font-size: 12px; color: #a0a0b0;');

