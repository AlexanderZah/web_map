import folium
from django.db.models import QuerySet

from web_map.models import MarkersModel


def add_markers_from_db() -> QuerySet:
    """
        Запрос маркеров из базы данных.

    """
    markers = MarkersModel.objects.select_related('category_layer').all()

    return markers


def create_icons_for_markers() -> dict:
    """
        Создание иконок для маркеров.
        Количество иконок должно быть равно количеству слоев в бд.

    """
    icons = {
        'Достопримечательности': (
            'blue',
            "glyphicon glyphicon-star",
            'glyphicon'),
        'Сбер': (
            'lightgreen',
            "fa-solid fa-ruble-sign",
            'fa'),
        'Парки': (
            'green',
            'glyphicon glyphicon-tree-deciduous',
            'glyphicon'),
    }

    return icons


def add_markers_for_layers(layers: dict) -> None:
    """
        Создания маркера и прикрепление его к опциональному слою на карте.

    """
    markers = add_markers_from_db()

    icons = create_icons_for_markers()

    for mark in markers:
        icon = icons.get(mark.category_layer.name)

        folium.Marker(
            location=[mark.longtitude, mark.latitude],
            popup=folium.Popup(mark.description, max_width=500),
            tooltip=mark.name,
            icon=folium.Icon(color=icon[0], icon=icon[1], prefix=icon[2])
        ).add_to(layers.get(mark.category_layer.name))
