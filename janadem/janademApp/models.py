from django.db import models

class UserModel(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords
