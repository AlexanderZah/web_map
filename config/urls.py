
from django.contrib import admin
from django.urls import path, include
import web_map


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_map.urls')),
    
]
