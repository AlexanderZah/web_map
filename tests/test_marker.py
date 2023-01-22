import pytest

from service_map import marker
from web_map.models import MarkersModel, LayersModel


@pytest.mark.django_db
def test_add_markers_from_db():
    res = marker.add_markers_from_db()
    expected = MarkersModel.objects.all()
    assert len(res) == len(expected)


@pytest.mark.django_db
def test_create_icons_for_markers():
    res = marker.create_icons_for_markers()
    expected = LayersModel.objects.all()
    assert len(res) == len(expected)



