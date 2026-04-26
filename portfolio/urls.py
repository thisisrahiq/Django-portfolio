from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout, name='admin_logout'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
