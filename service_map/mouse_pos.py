from folium.plugins import MousePosition


def add_mouse_position(city_nn_map):
    """
        Координаты позиции мыши на карте.

    """

    formatter = "function(num) {return L.Util.formatNum(num, 5);};"
    mouse_position = MousePosition(
        position='topright',
        separator=' Долг: ',
        empty_string='NaN',
        lng_first=False,
        num_digits=20,
        prefix='Шир:',
        lat_formatter=formatter,
        lng_formatter=formatter,
    )

    city_nn_map.add_child(mouse_position)
