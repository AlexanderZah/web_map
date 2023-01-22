import pytest

from service_map import marker
from web_map.models import MarkersModel, LayersModel


@pytest.mark.django_db
def test_create_icons_for_markers():
    """
        Для каждого слоя своя иконка на маркере.
        Количество иконок равно количеству слоев.

    """
    res = marker.create_icons_for_markers()
    expected = LayersModel.objects.all().count()
    assert len(res) == expected


@pytest.mark.django_db
def test_add_markers_from_db():
    """
        Количество созданных маркеров равно кол-ву маркеров из бд.
    """
    res = marker.add_markers_from_db()
    expected = MarkersModel.objects.all().count()
    assert len(res) == expected



