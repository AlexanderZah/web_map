from service_map.layer import create_groups_layers
import pytest
import folium





@pytest.mark.parametrize("my_map, layers",[(folium.Map([32.3, 54.2]), ('Парки', 'Скверы', 'Дома')), 
                            (folium.Map([00.21, 154.2]), ('Рестораны', 'Магазины', 'Аттракционы')),
                            ])
def test_create_groups_layers_good(my_map, layers):
    res = create_groups_layers(my_map, layers)
    assert res != list()
