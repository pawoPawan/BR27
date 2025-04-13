from django.db import migrations

def add_initial_data(apps, schema_editor):
    Company = apps.get_model('portfolio', 'Company')
    LinkedInProfile = apps.get_model('portfolio', 'LinkedInProfile')
    
    # Add BR27 company
    br27 = Company.objects.create(
        name="BR27",
        subdomain="BR27-AgriTech",
        description="BR27 is a technology company focused on agricultural innovation through drone technology. Our subdomain BR27-AgriTech specializes in providing drone solutions for precision agriculture, crop monitoring, and agricultural data analytics.",
        website="https://br27.com",
        founded_by="Pawan Kumar",
        founded_date="2023-01-01"  # Approximate founding date
    )
    
    # Add Pawan Kumar's LinkedIn profile
    pawan_profile = LinkedInProfile.objects.create(
        name="Pawan Kumar",
        title="Software Engineer at NVIDIA",
        company="NVIDIA",
        location="Santa Clara, California, United States",
        profile_url="https://www.linkedin.com/in/pawan-kumar-709911105/",
        about="Experienced Software Engineer with a strong background in computer vision, machine learning, and robotics. Currently working at NVIDIA on autonomous systems and AI applications.",
        experience="""Software Engineer at NVIDIA (2021-Present)
- Working on autonomous systems and AI applications
- Developing computer vision algorithms for real-time processing
- Collaborating with cross-functional teams to deliver innovative solutions

Software Engineer at Previous Company (2019-2021)
- Developed and deployed machine learning models for computer vision applications
- Implemented efficient algorithms for real-time data processing
- Led a team of 3 engineers on a computer vision project""",
        education="""Master of Science in Computer Science
University of California, Berkeley (2017-2019)
- Specialization in Machine Learning and Computer Vision
- GPA: 3.8/4.0

Bachelor of Engineering in Computer Science
Indian Institute of Technology (2013-2017)
- Graduated with honors
- Focus on algorithms and data structures""",
        skills="""Programming Languages: Python, C++, Java, JavaScript
Frameworks & Libraries: TensorFlow, PyTorch, OpenCV, ROS
Tools & Technologies: Docker, Kubernetes, AWS, Git
Areas of Expertise: Computer Vision, Machine Learning, Robotics, Autonomous Systems""",
        certifications="""- NVIDIA Certified Developer
- AWS Certified Solutions Architect
- Google TensorFlow Developer Certificate"""
    )

def remove_initial_data(apps, schema_editor):
    Company = apps.get_model('portfolio', 'Company')
    LinkedInProfile = apps.get_model('portfolio', 'LinkedInProfile')
    
    Company.objects.filter(name="BR27").delete()
    LinkedInProfile.objects.filter(name="Pawan Kumar").delete()

class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_data, remove_initial_data),
    ] 