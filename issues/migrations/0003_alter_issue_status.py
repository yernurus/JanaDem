# Generated by Django 3.2.25 on 2024-04-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_auto_20240404_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('0', 'CREATED'), ('1', 'SENT'), ('2', 'APPROVED'), ('3', 'REJECTED'), ('4', 'IN_PROGRESS'), ('5', 'FINISHED')], max_length=20),
        ),
    ]
