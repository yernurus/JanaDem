from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=100) 
    birth_date = models.DateField()
    
    class Meta:
        db_table = 'users'

        app_label = 'Users'
        managed = False