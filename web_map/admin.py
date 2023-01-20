from django.contrib import admin
from .models import LayersModel, MarkersModel


admin.site.register(MarkersModel)
admin.site.register(LayersModel)

