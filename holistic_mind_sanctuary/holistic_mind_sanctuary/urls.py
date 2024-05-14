from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sanctuary.urls')),  # Changed to include at the root
    # Other app URLs can be included here as well
]
