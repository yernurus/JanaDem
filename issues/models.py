from django.db import models
from account.models import User
from issues import IssueStatus


# Create your models here.
class Issue(models.Model):
    image = models.ImageField(upload_to='issue_photos/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.CharField(max_length=20, null=False, choices=IssueStatus.choices)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'
        db_table = 'Issue'