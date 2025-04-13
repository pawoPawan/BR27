from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)  # 1-5 scale
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    subdomain = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    website = models.URLField(blank=True)
    founded_by = models.CharField(max_length=200)
    founded_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LinkedInProfile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    profile_url = models.URLField()
    profile_image = models.ImageField(upload_to='linkedin/', blank=True, null=True)
    about = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    certifications = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Subdivision(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Block(models.Model):
    name = models.CharField(max_length=100)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE, related_name='blocks')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.subdivision.name}"

    class Meta:
        ordering = ['name']

class GramPanchayat(models.Model):
    name = models.CharField(max_length=100)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='gram_panchayats')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.block.name}"

    class Meta:
        ordering = ['name']

class Village(models.Model):
    name = models.CharField(max_length=100)
    gram_panchayat = models.ForeignKey(GramPanchayat, on_delete=models.CASCADE, related_name='villages')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.gram_panchayat.name}"

    class Meta:
        ordering = ['name']

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='residents')
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    hobbies = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.village.name}"

    class Meta:
        ordering = ['user__first_name', 'user__last_name'] 