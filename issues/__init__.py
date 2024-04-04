from django.db import models


class IssueStatus(models.TextChoices):
    CREATED = 0, 'CREATED'
    SENT = 1, 'SENT'
    APPROVED = 2, 'APPROVED'
    REJECTED = 3, 'REJECTED'
    IN_PROGRESS = 4, 'IN_PROGRESS'
    FINISHED = 5, 'FINISHED'
