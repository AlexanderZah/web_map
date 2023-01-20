import folium
from web_map.models import LayersModel


def create_groups_layers(city) -> dict:
    group_layers = {}
    layers = LayersModel.objects.all()
    for lay in layers:
        layer = folium.FeatureGroup(name=lay.name)
        group_layers[lay.name] = layer
        layer.add_to(city)
    
    return group_layers


def add_layers(map):

    folium.TileLayer('cartodbpositron').add_to(map)
    folium.TileLayer('cartodbdark_matter').add_to(map)
    folium.TileLayer('stamentoner').add_to(map)
