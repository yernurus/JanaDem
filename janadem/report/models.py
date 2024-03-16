from django.db import models

# Create your models here.
class ReportModel(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'reports'
        app_label = 'Reports'
        managed = False

class Location(models.Model):  # Замените models.model на models.Model
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()