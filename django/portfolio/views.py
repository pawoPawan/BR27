from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import permission_classes
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Skill, LinkedInProfile, Company, Subdivision, Block, GramPanchayat, Village, UserProfile
from .serializers import ProjectSerializer, SkillSerializer, LinkedInProfileSerializer, CompanySerializer
from .forms import UserProfileForm

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LinkedInProfileViewSet(viewsets.ModelViewSet):
    queryset = LinkedInProfile.objects.all()
    serializer_class = LinkedInProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@permission_classes([AllowAny])
def portfolio_view(request):
    """
    View for the portfolio page that displays the executive team and technical team.
    """
    # Get executive team members
    executives = LinkedInProfile.objects.filter(title__icontains='chief').order_by('name')
    
    # Get agricultural experts
    agri_experts = LinkedInProfile.objects.filter(
        title__icontains='agricultural') | LinkedInProfile.objects.filter(
        title__icontains='crop') | LinkedInProfile.objects.filter(
        title__icontains='farm')
    
    # Get logistics experts
    logistics_experts = LinkedInProfile.objects.filter(
        title__icontains='logistics') | LinkedInProfile.objects.filter(
        title__icontains='delivery') | LinkedInProfile.objects.filter(
        title__icontains='operations')
    
    # Get technical team
    technical_team = LinkedInProfile.objects.filter(
        title__icontains='engineer') | LinkedInProfile.objects.filter(
        title__icontains='developer') | LinkedInProfile.objects.filter(
        title__icontains='scientist')
    
    context = {
        'executives': executives,
        'agri_experts': agri_experts,
        'logistics_experts': logistics_experts,
        'technical_team': technical_team,
    }
    
    return render(request, 'portfolio.html', context)

@permission_classes([AllowAny])
def company_view(request):
    company = Company.objects.filter(name="BR27").first()
    founder = LinkedInProfile.objects.filter(name="Pawan Kumar").first()
    
    context = {
        'company': company,
        'founder': founder,
    }
    
    return render(request, 'company.html', context)

@permission_classes([AllowAny])
def subdivision_list(request):
    subdivisions = Subdivision.objects.all()
    return render(request, 'portfolio/subdivision_list.html', {'subdivisions': subdivisions})

@permission_classes([AllowAny])
def block_list(request, subdivision_id):
    subdivision = get_object_or_404(Subdivision, id=subdivision_id)
    blocks = Block.objects.filter(subdivision=subdivision)
    return render(request, 'portfolio/block_list.html', {
        'subdivision': subdivision,
        'blocks': blocks
    })

@permission_classes([AllowAny])
def gram_panchayat_list(request, block_id):
    block = get_object_or_404(Block, id=block_id)
    gram_panchayats = GramPanchayat.objects.filter(block=block)
    return render(request, 'portfolio/gram_panchayat_list.html', {
        'block': block,
        'gram_panchayats': gram_panchayats
    })

@permission_classes([AllowAny])
def village_list(request, gram_panchayat_id):
    gram_panchayat = get_object_or_404(GramPanchayat, id=gram_panchayat_id)
    villages = Village.objects.filter(gram_panchayat=gram_panchayat)
    return render(request, 'portfolio/village_list.html', {
        'gram_panchayat': gram_panchayat,
        'villages': villages
    })

@permission_classes([AllowAny])
def village_detail(request, village_id):
    village = get_object_or_404(Village, id=village_id)
    profiles = UserProfile.objects.filter(village=village)
    return render(request, 'portfolio/village_detail.html', {
        'village': village,
        'profiles': profiles
    })

@login_required
def profile_create(request, village_id):
    village = get_object_or_404(Village, id=village_id)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.village = village
            profile.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('profile_detail', profile_id=profile.id)
    else:
        form = UserProfileForm()
    
    return render(request, 'portfolio/profile_form.html', {
        'form': form,
        'village': village,
        'action': 'Create'
    })

@login_required
def profile_edit(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id)
    
    if request.user != profile.user:
        messages.error(request, 'You do not have permission to edit this profile.')
        return redirect('profile_detail', profile_id=profile.id)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_detail', profile_id=profile.id)
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'portfolio/profile_form.html', {
        'form': form,
        'profile': profile,
        'action': 'Edit'
    })

@permission_classes([AllowAny])
def profile_detail(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id)
    return render(request, 'portfolio/profile_detail.html', {'profile': profile}) 