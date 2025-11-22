from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet, LinkedInProfileViewSet, CompanyViewSet, company_view
from . import views
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'api/projects', ProjectViewSet)
router.register(r'api/skills', SkillViewSet)
router.register(r'api/linkedin', LinkedInProfileViewSet)
router.register(r'api/companies', CompanyViewSet)

urlpatterns = [
    path('', views.portfolio_view, name='portfolio'),
    path('company/', company_view, name='company'),
    path('subdivisions/', views.subdivision_list, name='subdivision_list'),
    path('subdivisions/<int:subdivision_id>/blocks/', views.block_list, name='block_list'),
    path('blocks/<int:block_id>/gram-panchayats/', views.gram_panchayat_list, name='gram_panchayat_list'),
    path('gram-panchayats/<int:gram_panchayat_id>/villages/', views.village_list, name='village_list'),
    path('villages/<int:village_id>/', views.village_detail, name='village_detail'),
    path('villages/<int:village_id>/profile/create/', views.profile_create, name='profile_create'),
    path('profiles/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('profiles/<int:profile_id>/edit/', views.profile_edit, name='profile_edit'),
    path('', include(router.urls)),
] 