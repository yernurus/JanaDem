from django.db import models
from django.contrib.auth.models import User as DjangoUser

class Report(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Point(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

class Bonus(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

class Merchandise(models.Model):
    name = models.CharField(max_length=100)
    points_required = models.IntegerField()
    description = models.TextField()

class Redemption(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    merchandise = models.ForeignKey(Merchandise, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)
