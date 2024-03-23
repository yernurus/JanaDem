from django.db import models

# Create your models here.
class Issue(models.Model):
    image = models.ImageField(upload_to='issue_photos/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    longitude = models.FloatField()
    latitude = models.FloatField()

    