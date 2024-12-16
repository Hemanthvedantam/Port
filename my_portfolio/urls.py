from django.contrib import admin
from django.urls import path, include  # Import include to include app-specific urls
from main import views # Import views if you need any direct references (not required for urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Include the URLs from the main app
]
