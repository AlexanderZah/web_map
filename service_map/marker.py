import folium
from .layer import create_groups_layers
from web_map.models import MarkersModel


def add_markers_for_layers(layers):
    """
        Создания маркера и прикрепление его к слою на карте
    """
    markers = MarkersModel.objects.select_related('category_layer').all()
    
    icons = {
        'Достопримечательности': ('blue', "glyphicon glyphicon-star"), 
        'Сбер': ('lightgreen', "glyphicon glyphicon-bold"),
        'Парки': ('green', 'glyphicon glyphicon-tree-deciduous'),
    }
    for mark in markers:
        icon = icons.get(mark.category_layer.name)
        
        folium.Marker(
            location=[mark.longtitude, mark.latitude],
            popup=folium.Popup(mark.description, max_width=500),
            tooltip=mark.name,
            icon=folium.Icon(color=icon[0], icon=icon[1])
        ).add_to(layers.get(mark.category_layer.name))
