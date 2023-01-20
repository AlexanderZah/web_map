from django.db import models


class LayersModel(models.Model):
    name = models.CharField(max_length=150)


class MarkersModel(models.Model):
    longtitude = models.FloatField()
    latitude = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    category_layer = models.ForeignKey(
        LayersModel,
        on_delete=models.DO_NOTHING,
        null=True
        )

# class SberMarkersModel(models.Model):
#     longtitude = models.FloatField()
#     latitude = models.FloatField()
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     category_layer = models.ForeignKey(
#         LayersModel,
#         on_delete=models.DO_NOTHING,
#         null=True
#         )


# class SightsMarkersModel(models.Model):
#     longtitude = models.FloatField()
#     latitude = models.FloatField()
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     category_layer = models.ForeignKey(
#         LayersModel,
#         on_delete=models.DO_NOTHING,
#         null=True
#         )


# class ParksMarkersModel(models.Model):
#     longtitude = models.FloatField()
#     latitude = models.FloatField()
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     category_layer = models.ForeignKey(
#         LayersModel,
#         on_delete=models.DO_NOTHING,
#         null=True
#         )
