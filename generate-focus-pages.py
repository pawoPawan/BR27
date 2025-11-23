#!/usr/bin/env python3
"""
Generate all focus area pages for BR27 website
Each page has unique theme colors and content
"""

focus_areas = {
    "technology": {
        "title": "Technology",
        "title_hi": "प्रौद्योगिकी",
        "subtitle": "Demystifying digital tools and emerging tech to help communities stay ahead in an ever-evolving landscape.",
        "subtitle_hi": "डिजिटल टूल और उभरती तकनीक को सरल बनाना ताकि समुदाय लगातार बदलते परिदृश्य में आगे रह सकें।",
        "gradient": "#667eea 0%, #764ba2 100%",
        "mission_title": "Empowering Through Technology",
        "mission_title_hi": "प्रौद्योगिकी के माध्यम से सशक्तिकरण",
        "areas": [
            {
                "icon": "💻",
                "title": "Digital Literacy",
                "title_hi": "डिजिटल साक्षरता",
                "text": "Building foundational digital skills for all ages",
                "text_hi": "सभी उम्र के लिए बुनियादी डिजिटल कौशल का निर्माण"
            },
            {
                "icon": "🤖",
                "title": "AI & Automation",
                "title_hi": "AI और ऑटोमेशन",
                "text": "Understanding artificial intelligence and its applications",
                "text_hi": "कृत्रिम बुद्धिमत्ता और इसके अनुप्रयोगों को समझना"
            },
            {
                "icon": "☁️",
                "title": "Cloud Computing",
                "title_hi": "क्लाउड कंप्यूटिंग",
                "text": "Leveraging cloud technology for business and personal use",
                "text_hi": "व्यवसाय और व्यक्तिगत उपयोग के लिए क्लाउड प्रौद्योगिकी का लाभ उठाना"
            }
        ]
    },
    "governance": {
        "title": "Governance",
        "title_hi": "शासन",
        "subtitle": "Bringing transparency and understanding to policies, rights, and civic engagement for informed participation.",
        "subtitle_hi": "नीतियों, अधिकारों और नागरिक भागीदारी में पारदर्शिता और समझ लाना ताकि सूचित भागीदारी हो सके।",
        "gradient": "#4facfe 0%, #00f2fe 100%",
        "mission_title": "Building Informed Citizens",
        "mission_title_hi": "सूचित नागरिकों का निर्माण",
        "areas": [
            {
                "icon": "🏛️",
                "title": "Civic Rights",
                "title_hi": "नागरिक अधिकार",
                "text": "Understanding fundamental rights and responsibilities",
                "text_hi": "मौलिक अधिकारों और जिम्मेदारियों को समझना"
            },
            {
                "icon": "📜",
                "title": "Government Schemes",
                "title_hi": "सरकारी योजनाएं",
                "text": "Access to welfare programs and benefits",
                "text_hi": "कल्याण कार्यक्रमों और लाभों तक पहुंच"
            },
            {
                "icon": "🗳️",
                "title": "Democratic Participation",
                "title_hi": "लोकतांत्रिक भागीदारी",
                "text": "Engaging effectively in democratic processes",
                "text_hi": "लोकतांत्रिक प्रक्रियाओं में प्रभावी ढंग से भाग लेना"
            }
        ]
    },
    "skills-development": {
        "title": "Skills Development",
        "title_hi": "कौशल विकास",
        "subtitle": "Practical training and insights to build competencies that matter in today's job market and entrepreneurship.",
        "subtitle_hi": "व्यावहारिक प्रशिक्षण और अंतर्दृष्टि जो आज के नौकरी बाजार और उद्यमिता में मायने रखने वाली दक्षताओं का निर्माण करती है।",
        "gradient": "#f093fb 0%, #f5576c 100%",
        "mission_title": "Empowering Through Skills",
        "mission_title_hi": "कौशल के माध्यम से सशक्तिकरण",
        "areas": [
            {
                "icon": "🎯",
                "title": "Vocational Training",
                "title_hi": "व्यावसायिक प्रशिक्षण",
                "text": "Hands-on training for in-demand trades",
                "text_hi": "मांग वाले व्यापारों के लिए व्यावहारिक प्रशिक्षण"
            },
            {
                "icon": "💼",
                "title": "Professional Skills",
                "title_hi": "पेशेवर कौशल",
                "text": "Communication, leadership, and workplace competencies",
                "text_hi": "संचार, नेतृत्व और कार्यस्थल दक्षताएं"
            },
            {
                "icon": "🚀",
                "title": "Entrepreneurship",
                "title_hi": "उद्यमिता",
                "text": "Building and scaling your own business",
                "text_hi": "अपना खुद का व्यवसाय बनाना और बढ़ाना"
            }
        ]
    },
    "financial-awareness": {
        "title": "Financial Awareness",
        "title_hi": "वित्तीय जागरूकता",
        "subtitle": "Building financial literacy from basics to smart investments, helping people make confident money decisions.",
        "subtitle_hi": "बुनियादी बातों से लेकर स्मार्ट निवेश तक वित्तीय साक्षरता का निर्माण, लोगों को आत्मविश्वास से पैसे के फैसले लेने में मदद करना।",
        "gradient": "#fa709a 0%, #fee140 100%",
        "mission_title": "Financial Empowerment for All",
        "mission_title_hi": "सभी के लिए वित्तीय सशक्तिकरण",
        "areas": [
            {
                "icon": "💰",
                "title": "Budgeting & Saving",
                "title_hi": "बजट और बचत",
                "text": "Managing money effectively and building savings",
                "text_hi": "पैसे का प्रभावी ढंग से प्रबंधन और बचत बनाना"
            },
            {
                "icon": "📈",
                "title": "Investment Basics",
                "title_hi": "निवेश मूल बातें",
                "text": "Understanding stocks, mutual funds, and wealth creation",
                "text_hi": "स्टॉक, म्यूचुअल फंड और धन सृजन को समझना"
            },
            {
                "icon": "🏦",
                "title": "Banking & Credit",
                "title_hi": "बैंकिंग और ऋण",
                "text": "Navigating banking services and credit management",
                "text_hi": "बैंकिंग सेवाओं और ऋण प्रबंधन को नेविगेट करना"
            }
        ]
    },
    "education-careers": {
        "title": "Education Paths & Careers",
        "title_hi": "शिक्षा पथ और करियर",
        "subtitle": "Guiding students through educational choices, career opportunities, and pathways to success in their chosen fields.",
        "subtitle_hi": "छात्रों को शैक्षिक विकल्पों, करियर के अवसरों और उनके चुने हुए क्षेत्रों में सफलता के मार्गों के माध्यम से मार्गदर्शन करना।",
        "gradient": "#feca57 0%, #ff9068 100%",
        "mission_title": "Charting Your Career Path",
        "mission_title_hi": "अपने करियर पथ का निर्धारण",
        "areas": [
            {
                "icon": "🎓",
                "title": "Higher Education",
                "title_hi": "उच्च शिक्षा",
                "text": "Choosing the right courses and institutions",
                "text_hi": "सही पाठ्यक्रम और संस्थानों का चयन"
            },
            {
                "icon": "🧭",
                "title": "Career Counseling",
                "title_hi": "करियर परामर्श",
                "text": "Finding the right career path for your skills and interests",
                "text_hi": "आपके कौशल और रुचियों के लिए सही करियर पथ खोजना"
            },
            {
                "icon": "📚",
                "title": "Skill Certifications",
                "title_hi": "कौशल प्रमाणन",
                "text": "Industry-recognized credentials and certifications",
                "text_hi": "उद्योग-मान्यता प्राप्त प्रमाण पत्र और प्रमाणन"
            }
        ]
    }
}

print("Focus areas data structure ready!")
print(f"Total focus areas: {len(focus_areas)}")
for key in focus_areas:
    print(f"- {focus_areas[key]['title']}")

