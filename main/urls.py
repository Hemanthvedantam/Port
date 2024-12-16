from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('introduction/', views.introduction, name='introduction'),
    path('technologies/', views.technologies, name='technologies'),
    path('certifications/', views.certifications, name='certifications'),
    path('coding_profiles/', views.coding_profiles, name='coding_profiles'),
    path('hero/', views.hero_page, name='hero_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
