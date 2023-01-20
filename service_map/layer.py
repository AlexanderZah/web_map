import folium


layers = (
    'Достопримечательности',
    'Сбер',
    'Парки'
)


def create_groups_layers(city, layers) -> list:
    group_layers = []

    for lay in layers:
        layer = folium.FeatureGroup(name=lay)
        group_layers.append(layer)
        layer.add_to(city)
    
    return group_layers


def add_layers(map):

    folium.TileLayer('cartodbpositron').add_to(map)
    folium.TileLayer('cartodbdark_matter').add_to(map)
    folium.TileLayer('stamentoner').add_to(map)
