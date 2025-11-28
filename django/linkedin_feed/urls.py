"""
LinkedIn Feed URL Configuration
"""
from django.urls import path
from . import views

app_name = 'linkedin_feed'

urlpatterns = [
    path('posts/', views.fetch_linkedin_posts, name='fetch_posts'),
    path('status/', views.linkedin_feed_status, name='feed_status'),
]

