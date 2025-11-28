from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('api/linkedin/', include('linkedin_feed.urls')),  # LinkedIn feed API
    path('portfolio/', include('portfolio.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('auth/', TemplateView.as_view(template_name='auth.html'), name='auth'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 