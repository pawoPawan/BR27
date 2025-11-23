#!/usr/bin/env python3
"""
Generate custom focus area pages based on home.html descriptions
"""

import os

# Focus areas data with all content based on home.html data-translate attributes
focus_areas = {
    "technology": {
        "title_en": "Technology",
        "title_hi": "प्रौद्योगिकी",
        "subtitle_en": "Demystifying digital tools and emerging tech to help communities stay ahead in an ever-evolving landscape.",
        "subtitle_hi": "डिजिटल उपकरणों और उभरती तकनीक को सरल बनाना ताकि समुदाय लगातार बदलते परिदृश्य में आगे रह सकें।",
        "color": "#667eea",
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "icon": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/>',
        "mission_title_en": "Bridging the Digital Divide",
        "mission_title_hi": "डिजिटल विभाजन को पाटना",
        "mission_desc_en": "In today's fast-paced world, technology is transforming every aspect of our lives. BR27 is committed to demystifying complex digital tools and emerging technologies, making them accessible and understandable for everyone. We believe that when communities understand and embrace technology, they can unlock unprecedented opportunities for growth, innovation, and progress.",
        "mission_desc_hi": "आज की तेज़ गति वाली दुनिया में, प्रौद्योगिकी हमारे जीवन के हर पहलू को बदल रही है। BR27 जटिल डिजिटल उपकरणों और उभरती प्रौद्योगिकियों को सरल बनाने के लिए प्रतिबद्ध है, उन्हें सभी के लिए सुलभ और समझने योग्य बनाता है। हम मानते हैं कि जब समुदाय प्रौद्योगिकी को समझते और अपनाते हैं, तो वे विकास, नवाचार और प्रगति के लिए अभूतपूर्व अवसरों को अनलॉक कर सकते हैं।",
        "key_focus": [
            {"title_en": "Digital Literacy & Skills", "title_hi": "डिजिटल साक्षरता और कौशल", "desc_en": "Teaching essential digital skills from basic computer usage to advanced software applications, empowering people to participate confidently in the digital economy.", "desc_hi": "बुनियादी कंप्यूटर उपयोग से लेकर उन्नत सॉफ्टवेयर एप्लिकेशन तक आवश्यक डिजिटल कौशल सिखाना, लोगों को डिजिटल अर्थव्यवस्था में आत्मविश्वास से भाग लेने के लिए सशक्त बनाना।"},
            {"title_en": "Emerging Technologies", "title_hi": "उभरती प्रौद्योगिकियां", "desc_en": "Exploring cutting-edge innovations like AI, IoT, blockchain, and cloud computing, and understanding their real-world applications and potential impact.", "desc_hi": "एआई, आईओटी, ब्लॉकचेन और क्लाउड कंप्यूटिंग जैसी अत्याधुनिक नवाचारों की खोज करना, और उनके वास्तविक दुनिया के अनुप्रयोगों और संभावित प्रभाव को समझना।"},
            {"title_en": "Tech for Community Development", "title_hi": "सामुदायिक विकास के लिए तकनीक", "desc_en": "Leveraging technology to solve local challenges in education, healthcare, agriculture, and governance, creating sustainable community-driven solutions.", "desc_hi": "शिक्षा, स्वास्थ्य, कृषि और शासन में स्थानीय चुनौतियों को हल करने के लिए प्रौद्योगिकी का लाभ उठाना, टिकाऊ समुदाय-संचालित समाधान बनाना।"},
            {"title_en": "Cyber Safety & Security", "title_hi": "साइबर सुरक्षा और संरक्षा", "desc_en": "Building awareness about online safety, data privacy, and cybersecurity best practices to protect individuals and communities in the digital age.", "desc_hi": "डिजिटल युग में व्यक्तियों और समुदायों की रक्षा के लिए ऑनलाइन सुरक्षा, डेटा गोपनीयता और साइबर सुरक्षा सर्वोत्तम प्रथाओं के बारे में जागरूकता बढ़ाना।"}
        ]
    },
    "governance": {
        "title_en": "Governance",
        "title_hi": "शासन",
        "subtitle_en": "Bringing transparency and understanding to policies, rights, and civic engagement for informed participation.",
        "subtitle_hi": "नीतियों, अधिकारों और नागरिक भागीदारी में पारदर्शिता और समझ लाना ताकि सूचित भागीदारी हो सके।",
        "color": "#f093fb",
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "icon": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
        "mission_title_en": "Empowering Citizens Through Transparency",
        "mission_title_hi": "पारदर्शिता के माध्यम से नागरिकों को सशक्त बनाना",
        "mission_desc_en": "Good governance is the foundation of a thriving society. BR27 is dedicated to bringing transparency and understanding to government policies, citizen rights, and civic engagement opportunities. We simplify complex policies and regulations, helping people understand how they can actively participate in shaping their communities and holding their representatives accountable.",
        "mission_desc_hi": "सुशासन एक समृद्ध समाज की नींव है। BR27 सरकारी नीतियों, नागरिक अधिकारों और नागरिक जुड़ाव के अवसरों में पारदर्शिता और समझ लाने के लिए समर्पित है। हम जटिल नीतियों और विनियमों को सरल बनाते हैं, लोगों को समझने में मदद करते हैं कि वे अपने समुदायों को आकार देने और अपने प्रतिनिधियों को जवाबदेह ठहराने में सक्रिय रूप से कैसे भाग ले सकते हैं।",
        "key_focus": [
            {"title_en": "Policy Awareness", "title_hi": "नीति जागरूकता", "desc_en": "Breaking down government policies and schemes into simple, accessible language so citizens can understand and benefit from them.", "desc_hi": "सरकारी नीतियों और योजनाओं को सरल, सुलभ भाषा में तोड़ना ताकि नागरिक उन्हें समझ सकें और उनसे लाभान्वित हो सकें।"},
            {"title_en": "Citizen Rights & Responsibilities", "title_hi": "नागरिक अधिकार और जिम्मेदारियां", "desc_en": "Educating people about their fundamental rights, legal protections, and civic duties to foster responsible citizenship.", "desc_hi": "लोगों को उनके मौलिक अधिकारों, कानूनी संरक्षणों और नागरिक कर्तव्यों के बारे में शिक्षित करना ताकि जिम्मेदार नागरिकता को बढ़ावा दिया जा सके।"},
            {"title_en": "Civic Participation & Advocacy", "title_hi": "नागरिक भागीदारी और वकालत", "desc_en": "Encouraging active participation in local governance, elections, and community decision-making processes for democratic empowerment.", "desc_hi": "लोकतांत्रिक सशक्तिकरण के लिए स्थानीय शासन, चुनावों और सामुदायिक निर्णय लेने की प्रक्रियाओं में सक्रिय भागीदारी को प्रोत्साहित करना।"},
            {"title_en": "Transparency & Accountability", "title_hi": "पारदर्शिता और जवाबदेही", "desc_en": "Promoting transparency in governance and helping citizens understand how to hold their elected representatives and institutions accountable.", "desc_hi": "शासन में पारदर्शिता को बढ़ावा देना और नागरिकों को यह समझने में मदद करना कि वे अपने निर्वाचित प्रतिनिधियों और संस्थानों को कैसे जवाबदेह ठहरा सकते हैं।"}
        ]
    },
    "skills-development": {
        "title_en": "Skills Development",
        "title_hi": "कौशल विकास",
        "subtitle_en": "Practical training and insights to build competencies that matter in today's job market and entrepreneurship.",
        "subtitle_hi": "व्यावहारिक प्रशिक्षण और अंतर्दृष्टि जो आज के नौकरी बाजार और उद्यमिता में मायने रखने वाली दक्षताओं का निर्माण करती है।",
        "color": "#4facfe",
        "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
        "icon": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
        "mission_title_en": "Building Future-Ready Talent",
        "mission_title_hi": "भविष्य के लिए तैयार प्रतिभा का निर्माण",
        "mission_desc_en": "In a rapidly changing world, continuous skill development is essential for personal and professional growth. BR27 provides practical training and insights to help individuals build competencies that are in demand in today's job market and entrepreneurship landscape. We bridge the gap between traditional education and real-world requirements, preparing people for meaningful careers and successful ventures.",
        "mission_desc_hi": "तेजी से बदलती दुनिया में, व्यक्तिगत और व्यावसायिक विकास के लिए निरंतर कौशल विकास आवश्यक है। BR27 व्यक्तियों को उन दक्षताओं के निर्माण में मदद करने के लिए व्यावहारिक प्रशिक्षण और अंतर्दृष्टि प्रदान करता है जो आज के नौकरी बाजार और उद्यमिता परिदृश्य में मांग में हैं। हम पारंपरिक शिक्षा और वास्तविक दुनिया की आवश्यकताओं के बीच की खाई को पाटते हैं, लोगों को सार्थक करियर और सफल उद्यमों के लिए तैयार करते हैं।",
        "key_focus": [
            {"title_en": "Technical Skills Training", "title_hi": "तकनीकी कौशल प्रशिक्षण", "desc_en": "Hands-on training in in-demand technical skills including programming, data analysis, design, and more to boost career prospects.", "desc_hi": "करियर की संभावनाओं को बढ़ावा देने के लिए प्रोग्रामिंग, डेटा विश्लेषण, डिजाइन और अधिक सहित मांग वाले तकनीकी कौशल में व्यावहारिक प्रशिक्षण।"},
            {"title_en": "Soft Skills & Communication", "title_hi": "सॉफ्ट स्किल्स और संचार", "desc_en": "Developing essential soft skills like communication, leadership, teamwork, and problem-solving crucial for workplace success.", "desc_hi": "कार्यस्थल की सफलता के लिए महत्वपूर्ण संचार, नेतृत्व, टीमवर्क और समस्या-समाधान जैसे आवश्यक सॉफ्ट कौशल विकसित करना।"},
            {"title_en": "Entrepreneurship Fundamentals", "title_hi": "उद्यमिता मूल बातें", "desc_en": "Equipping aspiring entrepreneurs with business planning, marketing, financial management, and innovation skills to launch successful ventures.", "desc_hi": "महत्वाकांक्षी उद्यमियों को सफल उद्यम शुरू करने के लिए व्यवसाय योजना, विपणन, वित्तीय प्रबंधन और नवाचार कौशल से लैस करना।"},
            {"title_en": "Career Readiness & Job Search", "title_hi": "करियर तत्परता और नौकरी खोज", "desc_en": "Preparing individuals for the job market with resume building, interview skills, networking strategies, and professional development guidance.", "desc_hi": "रिज्यूमे निर्माण, साक्षात्कार कौशल, नेटवर्किंग रणनीतियों और पेशेवर विकास मार्गदर्शन के साथ नौकरी बाजार के लिए व्यक्तियों को तैयार करना।"}
        ]
    },
    "rural-development": {
        "title_en": "Rural Development",
        "title_hi": "ग्रामीण विकास",
        "subtitle_en": "Empowering rural communities with knowledge, resources, and pathways to sustainable growth and prosperity.",
        "subtitle_hi": "ग्रामीण समुदायों को ज्ञान, संसाधन और टिकाऊ विकास और समृद्धि के मार्गों के साथ सशक्त बनाना।",
        "color": "#43e97b",
        "gradient": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
        "icon": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
        "mission_title_en": "Transforming Rural Communities",
        "mission_title_hi": "ग्रामीण समुदायों का परिवर्तन",
        "mission_desc_en": "Rural communities are the backbone of our nation, yet they often lack access to information, resources, and opportunities. BR27 is committed to empowering rural communities with knowledge, resources, and pathways to sustainable growth and prosperity. We believe that when rural areas thrive, the entire nation benefits from increased economic activity, innovation, and social progress.",
        "mission_desc_hi": "ग्रामीण समुदाय हमारे राष्ट्र की रीढ़ हैं, फिर भी उन्हें अक्सर जानकारी, संसाधनों और अवसरों तक पहुंच की कमी होती है। BR27 ग्रामीण समुदायों को ज्ञान, संसाधनों और टिकाऊ विकास और समृद्धि के मार्गों के साथ सशक्त बनाने के लिए प्रतिबद्ध है। हम मानते हैं कि जब ग्रामीण क्षेत्र समृद्ध होते हैं, तो पूरा राष्ट्र बढ़ी हुई आर्थिक गतिविधि, नवाचार और सामाजिक प्रगति से लाभान्वित होता है।",
        "key_focus": [
            {"title_en": "Agricultural Innovation", "title_hi": "कृषि नवाचार", "desc_en": "Introducing modern farming techniques, sustainable practices, and agricultural technology to improve productivity and farmer livelihoods.", "desc_hi": "उत्पादकता और किसान आजीविका में सुधार के लिए आधुनिक खेती तकनीकों, टिकाऊ प्रथाओं और कृषि प्रौद्योगिकी की शुरुआत करना।"},
            {"title_en": "Rural Infrastructure & Connectivity", "title_hi": "ग्रामीण बुनियादी ढांचा और कनेक्टिविटी", "desc_en": "Advocating for better infrastructure, digital connectivity, and access to essential services to bridge the urban-rural divide.", "desc_hi": "शहरी-ग्रामीण विभाजन को पाटने के लिए बेहतर बुनियादी ढांचे, डिजिटल कनेक्टिविटी और आवश्यक सेवाओं तक पहुंच की वकालत करना।"},
            {"title_en": "Rural Entrepreneurship", "title_hi": "ग्रामीण उद्यमिता", "desc_en": "Supporting rural entrepreneurs with business skills, market access, and resources to create local economic opportunities and employment.", "desc_hi": "स्थानीय आर्थिक अवसरों और रोजगार बनाने के लिए व्यावसायिक कौशल, बाजार पहुंच और संसाधनों के साथ ग्रामीण उद्यमियों का समर्थन करना।"},
            {"title_en": "Education & Healthcare Access", "title_hi": "शिक्षा और स्वास्थ्य सेवा पहुंच", "desc_en": "Working towards improved access to quality education and healthcare facilities in rural areas for holistic community development.", "desc_hi": "समग्र सामुदायिक विकास के लिए ग्रामीण क्षेत्रों में गुणवत्तापूर्ण शिक्षा और स्वास्थ्य सेवा सुविधाओं तक बेहतर पहुंच की दिशा में काम करना।"}
        ]
    },
    "financial-awareness": {
        "title_en": "Financial Awareness",
        "title_hi": "वित्तीय जागरूकता",
        "subtitle_en": "Building financial literacy from basics to smart investments, helping people make confident money decisions.",
        "subtitle_hi": "बुनियादी बातों से लेकर स्मार्ट निवेश तक वित्तीय साक्षरता का निर्माण, लोगों को आत्मविश्वास से पैसे के फैसले लेने में मदद करना।",
        "color": "#fa709a",
        "gradient": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)",
        "icon": '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
        "mission_title_en": "Empowering Financial Independence",
        "mission_title_hi": "वित्तीय स्वतंत्रता को सशक्त बनाना",
        "mission_desc_en": "Financial literacy is the key to economic security and personal empowerment. BR27 is dedicated to building financial awareness from the basics of budgeting and saving to smart investments and wealth creation. We demystify complex financial concepts, helping people make confident, informed money decisions that can transform their lives and secure their futures.",
        "mission_desc_hi": "वित्तीय साक्षरता आर्थिक सुरक्षा और व्यक्तिगत सशक्तिकरण की कुंजी है। BR27 बजट और बचत की मूल बातों से लेकर स्मार्ट निवेश और धन सृजन तक वित्तीय जागरूकता बनाने के लिए समर्पित है। हम जटिल वित्तीय अवधारणाओं को सरल बनाते हैं, लोगों को आत्मविश्वास से, सूचित धन निर्णय लेने में मदद करते हैं जो उनके जीवन को बदल सकते हैं और उनके भविष्य को सुरक्षित कर सकते हैं।",
        "key_focus": [
            {"title_en": "Budgeting & Saving Fundamentals", "title_hi": "बजट और बचत मूल बातें", "desc_en": "Teaching practical budgeting strategies, saving habits, and expense management to build a strong financial foundation.", "desc_hi": "एक मजबूत वित्तीय नींव बनाने के लिए व्यावहारिक बजट रणनीतियों, बचत आदतों और खर्च प्रबंधन को सिखाना।"},
            {"title_en": "Investment & Wealth Creation", "title_hi": "निवेश और धन सृजन", "desc_en": "Understanding investment options, risk management, and wealth-building strategies from stocks and mutual funds to real estate.", "desc_hi": "स्टॉक और म्यूचुअल फंड से लेकर रियल एस्टेट तक निवेश विकल्पों, जोखिम प्रबंधन और धन-निर्माण रणनीतियों को समझना।"},
            {"title_en": "Financial Planning & Goals", "title_hi": "वित्तीय योजना और लक्ष्य", "desc_en": "Creating comprehensive financial plans aligned with life goals, including retirement planning, children's education, and emergency funds.", "desc_hi": "सेवानिवृत्ति योजना, बच्चों की शिक्षा और आपातकालीन निधि सहित जीवन लक्ष्यों के साथ संरेखित व्यापक वित्तीय योजनाएं बनाना।"},
            {"title_en": "Digital Finance & Banking", "title_hi": "डिजिटल वित्त और बैंकिंग", "desc_en": "Navigating digital payment systems, online banking, and fintech solutions safely and effectively for modern financial management.", "desc_hi": "आधुनिक वित्तीय प्रबंधन के लिए डिजिटल भुगतान प्रणाली, ऑनलाइन बैंकिंग और फिनटेक समाधानों को सुरक्षित और प्रभावी ढंग से नेविगेट करना।"}
        ]
    },
    "education-careers": {
        "title_en": "Education Paths & Careers",
        "title_hi": "शिक्षा पथ और करियर",
        "subtitle_en": "Guiding students through educational choices, career opportunities, and pathways to success in their chosen fields.",
        "subtitle_hi": "छात्रों को शैक्षिक विकल्पों, करियर के अवसरों और उनके चुने हुए क्षेत्रों में सफलता के मार्गों के माध्यम से मार्गदर्शन करना।",
        "color": "#feca57",
        "gradient": "linear-gradient(135deg, #feca57 0%, #ff9068 100%)",
        "icon": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
        "mission_title_en": "Navigating Your Future",
        "mission_title_hi": "अपने भविष्य को नेविगेट करना",
        "mission_desc_en": "Choosing the right educational path and career can be overwhelming. BR27 provides comprehensive guidance to students through educational choices, career opportunities, and pathways to success in their chosen fields. We help students understand their options, align their passions with practical career paths, and make informed decisions that set them up for long-term success and fulfillment.",
        "mission_desc_hi": "सही शैक्षिक पथ और करियर चुनना भारी हो सकता है। BR27 छात्रों को शैक्षिक विकल्पों, करियर के अवसरों और उनके चुने हुए क्षेत्रों में सफलता के मार्गों के माध्यम से व्यापक मार्गदर्शन प्रदान करता है। हम छात्रों को उनके विकल्पों को समझने, उनके जुनून को व्यावहारिक करियर मार्गों के साथ संरेखित करने और ऐसे सूचित निर्णय लेने में मदद करते हैं जो उन्हें दीर्घकालिक सफलता और पूर्ति के लिए तैयार करते हैं।",
        "key_focus": [
            {"title_en": "Academic Streams & Higher Education", "title_hi": "शैक्षणिक धाराएं और उच्च शिक्षा", "desc_en": "Guiding students through choosing the right academic stream and higher education options aligned with their interests and career goals.", "desc_hi": "छात्रों को उनकी रुचियों और करियर लक्ष्यों के साथ संरेखित सही शैक्षणिक धारा और उच्च शिक्षा विकल्प चुनने में मार्गदर्शन करना।"},
            {"title_en": "Career Exploration & Planning", "title_hi": "करियर अन्वेषण और योजना", "desc_en": "Exploring diverse career fields, understanding job roles, industry trends, and required skills to make informed career choices.", "desc_hi": "विविध करियर क्षेत्रों की खोज करना, नौकरी की भूमिकाओं, उद्योग के रुझानों और आवश्यक कौशल को समझना ताकि सूचित करियर विकल्प बनाए जा सकें।"},
            {"title_en": "Competitive Exams & Admissions", "title_hi": "प्रतियोगी परीक्षाएं और प्रवेश", "desc_en": "Providing guidance on preparing for competitive exams, entrance tests, and navigating college admissions processes effectively.", "desc_hi": "प्रतियोगी परीक्षाओं की तैयारी, प्रवेश परीक्षणों और कॉलेज प्रवेश प्रक्रियाओं को प्रभावी ढंग से नेविगेट करने पर मार्गदर्शन प्रदान करना।"},
            {"title_en": "Career Transitions & Growth", "title_hi": "करियर परिवर्तन और विकास", "desc_en": "Supporting professionals in career transitions, skill upgradation, and continuous learning for sustained career growth and fulfillment.", "desc_hi": "निरंतर करियर विकास और पूर्ति के लिए करियर परिवर्तन, कौशल उन्नयन और निरंतर सीखने में पेशेवरों का समर्थन करना।"}
        ]
    }
}

# Base output directory
base_dir = os.path.dirname(os.path.abspath(__file__))

print("🚀 Generating custom focus area pages...")
print("=" * 60)

for slug, data in focus_areas.items():
    print(f"\n📄 Creating {slug} page...")
    
    # Generate HTML
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="BR27 {data['title_en']} - {data['subtitle_en']}">
    <title>{data['title_en']} | BR27</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="{slug}.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="container nav-container">
            <div class="logo">
                <a href="/home" class="logo-link">
                    <span class="logo-text">BR27</span>
                </a>
            </div>
            <ul class="nav-menu" id="navMenu">
                <li><a href="/home" class="nav-link" data-translate="nav.home">Home</a></li>
                <li><a href="/home#about" class="nav-link" data-translate="nav.about">About</a></li>
                <li><a href="/home#focus" class="nav-link" data-translate="nav.focus">Focus Areas</a></li>
                <li><a href="/home#contact" class="nav-link" data-translate="nav.contact">Contact</a></li>
            </ul>
            <div class="nav-actions">
                <button id="languageToggle" class="language-toggle" aria-label="Switch Language">
                    <span class="lang-icon">🌐</span>
                    <span class="lang-text" id="langText">हिंदी</span>
                </button>
                <div class="hamburger" id="hamburger">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="{slug}-hero page-hero">
        <div class="hero-background" style="background: {data['gradient']};"></div>
        <div class="container hero-content">
            <div class="breadcrumb">
                <a href="/home" data-translate="breadcrumb.home">Home</a>
                <span class="separator">›</span>
                <a href="/home#focus" data-translate="breadcrumb.focus">Focus Areas</a>
                <span class="separator">›</span>
                <span data-translate="breadcrumb.{slug}">{data['title_en']}</span>
            </div>
            <h1 class="page-title fade-in">
                <span class="highlight" data-translate="{slug}.hero.title">{data['title_en']}</span>
            </h1>
            <p class="page-subtitle fade-in-delay" data-translate="{slug}.hero.subtitle">
                {data['subtitle_en']}
            </p>
        </div>
    </section>

    <!-- Mission Section -->
    <section class="{slug}-mission section-padding">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" data-translate="{slug}.mission.tag">Our Mission</span>
                <h2 class="section-title" data-translate="{slug}.mission.title">{data['mission_title_en']}</h2>
            </div>
            <div class="mission-content">
                <p class="mission-description" data-translate="{slug}.mission.desc">
                    {data['mission_desc_en']}
                </p>
            </div>
        </div>
    </section>

    <!-- Key Focus Areas -->
    <section class="{slug}-focus section-padding">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" data-translate="{slug}.focus.tag">Key Focus Areas</span>
                <h2 class="section-title" data-translate="{slug}.focus.title">How We Make a Difference</h2>
            </div>
            <div class="focus-grid">'''
    
    # Add focus cards
    for i, focus in enumerate(data['key_focus']):
        html_content += f'''
                <div class="focus-card">
                    <div class="focus-card-icon" style="background: {data['gradient']};">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            {data['icon']}
                        </svg>
                    </div>
                    <h3 data-translate="{slug}.focus.area{i+1}.title">{focus['title_en']}</h3>
                    <p data-translate="{slug}.focus.area{i+1}.desc">
                        {focus['desc_en']}
                    </p>
                </div>'''
    
    html_content += f'''
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta">
        <div class="container">
            <div class="cta-content">
                <h2 data-translate="{slug}.cta.title">Ready to Get Started?</h2>
                <p data-translate="{slug}.cta.text">Join us in our mission to empower communities through knowledge and practical insights.</p>
                <div class="cta-buttons">
                    <a href="/home#contact" class="btn btn-primary btn-large" data-translate="{slug}.cta.btn1">Get in Touch</a>
                    <a href="/home#about" class="btn btn-outline btn-large" data-translate="{slug}.cta.btn2">Learn More About BR27</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3 class="footer-logo">BR27</h3>
                    <p data-translate="footer.tagline">Empowering minds. Enabling progress.</p>
                    <div class="social-links">
                        <a href="https://www.linkedin.com/company/27br/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                                <rect x="2" y="9" width="4" height="12"/>
                                <circle cx="4" cy="4" r="2"/>
                            </svg>
                        </a>
                        <a href="https://www.youtube.com/@%E0%A4%AA%E0%A4%B2-%E0%A4%A6%E0%A5%8B-%E0%A4%AA%E0%A4%B2" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
                            </svg>
                        </a>
                    </div>
                </div>
                <div class="footer-section">
                    <h4 data-translate="footer.quicklinks">Quick Links</h4>
                    <ul>
                        <li><a href="/home" data-translate="nav.home">Home</a></li>
                        <li><a href="/home#about" data-translate="nav.about">About</a></li>
                        <li><a href="/home#focus" data-translate="nav.focus">Focus Areas</a></li>
                        <li><a href="/home#contact" data-translate="nav.contact">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 data-translate="footer.focusareas">Focus Areas</h4>
                    <ul>
                        <li><a href="/technology" data-translate="focus.tech.title">Technology</a></li>
                        <li><a href="/governance" data-translate="focus.gov.title">Governance</a></li>
                        <li><a href="/skills-development" data-translate="focus.skills.title">Skills Development</a></li>
                        <li><a href="/rural-development" data-translate="focus.rural.title">Rural Development</a></li>
                        <li><a href="/financial-awareness" data-translate="focus.finance.title">Financial Awareness</a></li>
                        <li><a href="/education-careers" data-translate="focus.edu.title">Education & Careers</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 data-translate="footer.connect">Connect</h4>
                    <ul>
                        <li><a href="/home#contact" data-translate="footer.contactus">Contact Us</a></li>
                        <li><a href="https://www.linkedin.com/company/27br/" target="_blank">LinkedIn</a></li>
                        <li><a href="https://www.youtube.com/@%E0%A4%AA%E0%A4%B2-%E0%A4%A6%E0%A5%8B-%E0%A4%AA%E0%A4%B2" target="_blank">YouTube</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p data-translate="footer.copyright">&copy; 2025 BR27. All rights reserved. Building a confident, future-ready ecosystem.</p>
            </div>
        </div>
    </footer>

    <script src="script.js"></script>
    <script src="{slug}.js"></script>
</body>
</html>'''
    
    # Write HTML file
    with open(os.path.join(base_dir, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  ✓ Generated {slug}.html")
    
    # Generate CSS
    css_content = f'''/* ===== {data['title_en']} Page Styles ===== */

.{slug}-hero.page-hero {{
    background: {data['gradient']};
}}

.{slug}-hero .hero-background {{
    background: 
        radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
}}

.{slug}-mission {{
    background: var(--dark-surface);
}}

.{slug}-mission .mission-description {{
    font-size: 18px;
    line-height: 1.9;
    color: var(--text-secondary);
    max-width: 900px;
    margin: 40px auto 0;
    text-align: center;
}}

.{slug}-focus {{
    background: var(--dark-bg);
}}

.{slug}-focus .focus-card-icon {{
    background: {data['gradient']};
}}
'''
    
    # Write CSS file
    with open(os.path.join(base_dir, f"{slug}.css"), "w", encoding="utf-8") as f:
        f.write(css_content)
    print(f"  ✓ Generated {slug}.css")
    
    # Generate JS with translations
    js_translations_en = f'''        "nav.home": "Home",
        "nav.about": "About",
        "nav.focus": "Focus Areas",
        "nav.contact": "Contact",
        "breadcrumb.home": "Home",
        "breadcrumb.focus": "Focus Areas",
        "breadcrumb.{slug}": "{data['title_en']}",
        "{slug}.hero.title": "{data['title_en']}",
        "{slug}.hero.subtitle": "{data['subtitle_en']}",
        "{slug}.mission.tag": "Our Mission",
        "{slug}.mission.title": "{data['mission_title_en']}",
        "{slug}.mission.desc": "{data['mission_desc_en']}",
        "{slug}.focus.tag": "Key Focus Areas",
        "{slug}.focus.title": "How We Make a Difference",'''
    
    js_translations_hi = f'''        "nav.home": "होम",
        "nav.about": "हमारे बारे में",
        "nav.focus": "फोकस क्षेत्र",
        "nav.contact": "संपर्क करें",
        "breadcrumb.home": "होम",
        "breadcrumb.focus": "फोकस क्षेत्र",
        "breadcrumb.{slug}": "{data['title_hi']}",
        "{slug}.hero.title": "{data['title_hi']}",
        "{slug}.hero.subtitle": "{data['subtitle_hi']}",
        "{slug}.mission.tag": "हमारा मिशन",
        "{slug}.mission.title": "{data['mission_title_hi']}",
        "{slug}.mission.desc": "{data['mission_desc_hi']}",
        "{slug}.focus.tag": "मुख्य फोकस क्षेत्र",
        "{slug}.focus.title": "हम कैसे बदलाव लाते हैं",'''
    
    # Add focus area translations
    for i, focus in enumerate(data['key_focus']):
        js_translations_en += f'''
        "{slug}.focus.area{i+1}.title": "{focus['title_en']}",
        "{slug}.focus.area{i+1}.desc": "{focus['desc_en']}",'''
        js_translations_hi += f'''
        "{slug}.focus.area{i+1}.title": "{focus['title_hi']}",
        "{slug}.focus.area{i+1}.desc": "{focus['desc_hi']}",'''
    
    js_translations_en += f'''
        "{slug}.cta.title": "Ready to Get Started?",
        "{slug}.cta.text": "Join us in our mission to empower communities through knowledge and practical insights.",
        "{slug}.cta.btn1": "Get in Touch",
        "{slug}.cta.btn2": "Learn More About BR27",
        "footer.tagline": "Empowering minds. Enabling progress.",
        "footer.quicklinks": "Quick Links",
        "footer.focusareas": "Focus Areas",
        "footer.connect": "Connect",
        "footer.contactus": "Contact Us",
        "footer.copyright": "© 2025 BR27. All rights reserved. Building a confident, future-ready ecosystem.",
        "focus.tech.title": "Technology",
        "focus.gov.title": "Governance",
        "focus.skills.title": "Skills Development",
        "focus.rural.title": "Rural Development",
        "focus.finance.title": "Financial Awareness",
        "focus.edu.title": "Education & Careers"'''
    
    js_translations_hi += f'''
        "{slug}.cta.title": "शुरू करने के लिए तैयार हैं?",
        "{slug}.cta.text": "ज्ञान और व्यावहारिक अंतर्दृष्टि के माध्यम से समुदायों को सशक्त बनाने के हमारे मिशन में हमारे साथ शामिल हों।",
        "{slug}.cta.btn1": "संपर्क करें",
        "{slug}.cta.btn2": "BR27 के बारे में अधिक जानें",
        "footer.tagline": "मन को सशक्त बनाना। प्रगति को सक्षम बनाना।",
        "footer.quicklinks": "त्वरित लिंक",
        "footer.focusareas": "फोकस क्षेत्र",
        "footer.connect": "जुड़ें",
        "footer.contactus": "संपर्क करें",
        "footer.copyright": "© 2025 BR27. सर्वाधिकार सुरक्षित। एक आत्मविश्वासी, भविष्य के लिए तैयार पारिस्थितिकी तंत्र का निर्माण।",
        "focus.tech.title": "प्रौद्योगिकी",
        "focus.gov.title": "शासन",
        "focus.skills.title": "कौशल विकास",
        "focus.rural.title": "ग्रामीण विकास",
        "focus.finance.title": "वित्तीय जागरूकता",
        "focus.edu.title": "शिक्षा और करियर"'''
    
    js_content = f'''// Translations for {slug} page
const translations = {{
    en: {{
{js_translations_en}
    }},
    hi: {{
{js_translations_hi}
    }}
}};

let currentLanguage = localStorage.getItem('br27-language') || 'en';

function applyTranslations(lang) {{
    currentLanguage = lang;
    localStorage.setItem('br27-language', lang);
    document.documentElement.lang = lang;
    
    document.querySelectorAll('[data-translate]').forEach(element => {{
        const key = element.getAttribute('data-translate');
        if (translations[lang] && translations[lang][key]) {{
            element.textContent = translations[lang][key];
        }}
    }});
    
    const langText = document.getElementById('langText');
    if (langText) langText.textContent = lang === 'en' ? 'हिंदी' : 'English';
}}

// Apply saved language on page load
document.addEventListener('DOMContentLoaded', function() {{
    applyTranslations(currentLanguage);
    
    const languageToggle = document.getElementById('languageToggle');
    if (languageToggle) {{
        languageToggle.addEventListener('click', function() {{
            applyTranslations(currentLanguage === 'en' ? 'hi' : 'en');
        }});
    }}
    
    // Mobile Navigation Toggle
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');
    
    if (hamburger && navMenu) {{
        hamburger.addEventListener('click', () => {{
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        }});
    }}
    
    // Close menu when clicking on a link
    document.querySelectorAll('.nav-link').forEach(link => {{
        link.addEventListener('click', () => {{
            if (hamburger && navMenu) {{
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            }}
        }});
    }});
}});
'''
    
    # Write JS file
    with open(os.path.join(base_dir, f"{slug}.js"), "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"  ✓ Generated {slug}.js")

print("\n" + "=" * 60)
print("✅ All focus area pages generated successfully!")
print("=" * 60)

