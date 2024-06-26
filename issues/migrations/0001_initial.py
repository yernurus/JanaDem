# Generated by Django 3.2.25 on 2024-04-06 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='issue_photos/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('status', models.CharField(choices=[('0', 'CREATED'), ('1', 'SENT'), ('2', 'APPROVED'), ('3', 'REJECTED'), ('4', 'IN_PROGRESS'), ('5', 'FINISHED')], max_length=20)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
                'db_table': 'Issue',
            },
        ),
    ]
