from service_map import layer
import pytest
import folium
from web_map.models import LayersModel


@pytest.mark.django_db
@pytest.mark.parametrize("map", [folium.Map([32.3, 54.2]),
                                 (folium.Map([00.21, 154.2])),
                                 ])
def test_create_groups_layers_good(map):
    """
        Количество групп слоев равно количеству слоев в базе данных.

    """
    res = layer.create_groups_layers(map)
    expected = LayersModel.objects.all().count()

    assert len(res) == expected
