# Generated by Django 3.2.25 on 2024-04-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_rename_bonus_points_issuebonuspoint_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebonuspoint',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]
