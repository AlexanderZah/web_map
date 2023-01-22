import folium
from web_map.models import LayersModel


def create_groups_layers(map: folium.Map) -> dict:
    """
        Создание групп для объединия маркеров.

    """
    group_layers = {}
    layers = LayersModel.objects.all()

    for lay in layers:
        layer = folium.FeatureGroup(name=lay.name)
        group_layers[lay.name] = layer
        layer.add_to(map)

    return group_layers


def add_layers(map: folium.Map):
    """
        Добавление к карте базовых слоев.

    """

    folium.TileLayer(
        tiles='https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',
        attr='Map data: &copy; \
            <a href="https://www.openstreetmap.org/copyright">\
            OpenStreetMap\
            </a> contributors,\
            <a href="http://viewfinderpanoramas.org">SRTM</a>\
            | Map style: &copy; <a href="https://opentopomap.org">\
            OpenTopoMap\
            </a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">\
            CC-BY-SA</a>)',
        max_zoom=17,
        name='Рельеф'
    ).add_to(map)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS,\
            AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the\
            GIS User Community',
        name='Спутник',
    ).add_to(map)
