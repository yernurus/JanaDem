from django.db import models


class UserRole(models.TextChoices):
    USER = 'User', 'USER'
    MODERATOR = 'Moderator', 'MODERATOR'
    AKIMAT = 'Akimat', 'AKIMAT'
