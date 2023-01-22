import folium
from folium.plugins import LocateControl

from .mouse_pos import add_mouse_position
from .marker import add_markers_for_layers
from .layer import create_groups_layers, add_layers


def create_map_to_html():
    """
        Создание карты с координатами Нижнего Новгорода.
        Добавление на карту базовых слоев и опциональных слоев
        с маркерами(элементами на карте).
    """
    city_nn_map = folium.Map(
        location=[56.2927, 44.002],    # широта и долгота Нижнего Новгорода
        zoom_start=12,
        width='100%',
        height='100%',
        tiles=folium.TileLayer(name='Схема')

    )

    groups_layers = create_groups_layers(city_nn_map)
    add_markers_for_layers(groups_layers)
    add_layers(city_nn_map)
    folium.LayerControl().add_to(city_nn_map)

    # Отображение координат курсора
    add_mouse_position(city_nn_map)
    folium.LatLngPopup().add_to(city_nn_map)  

    # Местоположение пользователя
    LocateControl(
        strings={"title": "Местоположение", "popup": "Ваше местоположение"}
        ).add_to(city_nn_map)

    city_nn_map.get_root().html.add_child(folium.Element(
        """
        <div class="bottom-div"
            style="position:fixed;
            bottom: 0px; right: 0px; width: 100%; height:14px;
            background-color: white; z-index: 1100;">
        </div>
        """
    ))

    # Сохранение карты на html
    city_nn_map.save(r'web_map\templates\web_map\index.html')
