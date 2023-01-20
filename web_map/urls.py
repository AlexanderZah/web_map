from django.urls import path
from .views import index, element_detail


urlpatterns = [
   path('', index, name='index'),
]
