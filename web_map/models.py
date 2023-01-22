from django.db import models


class LayersModel(models.Model):
    """
        Модель для опциональных слоев на карте.
    """
    name = models.CharField(max_length=150)

    def get_all_objects(self):
        return LayersModel.objects.all()


class MarkersModel(models.Model):
    """
        Модель для маркеров(элементов) на карте.
    """
    longtitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    category_layer = models.ForeignKey(
        LayersModel,
        on_delete=models.DO_NOTHING,
        null=True
        )
