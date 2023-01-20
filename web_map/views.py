from django.shortcuts import render
from service_map import map_create


def index(request):
    map_create.create_map_to_html()
    return render(request, 'web_map/index.html')
