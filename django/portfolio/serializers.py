from rest_framework import serializers
from .models import Project, Skill, LinkedInProfile, Company

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class LinkedInProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedInProfile
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__' 