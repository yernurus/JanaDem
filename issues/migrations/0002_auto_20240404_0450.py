# Generated by Django 3.2.25 on 2024-04-03 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('1', 'CREATED'), ('2', 'SENT'), ('3', 'APPROVED'), ('4', 'REJECTED'), ('5', 'IN_PROGRESS'), ('6', 'FINISHED')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
