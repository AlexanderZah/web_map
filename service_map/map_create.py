import folium

from .mouse_pos import add_mouse_position
from .marker import add_markers_for_layers
from .layer import create_groups_layers, add_layers


def create_map_to_html():
    city_nn_map = folium.Map(
        location=[56.2927, 44.002],    # широта и долгота Нижнего Новгорода
        zoom_start=12,
        
    )

    groups_layers = create_groups_layers(city_nn_map)
    add_markers_for_layers(groups_layers)
    add_layers(city_nn_map)
    folium.LayerControl().add_to(city_nn_map)

    add_mouse_position(city_nn_map)
    city_nn_map.add_child(folium.LatLngPopup())

    city_nn_map.save(r'web_map\templates\web_map\index.html')

