# Generated by Django 3.2 on 2022-06-18 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0006_auto_20220618_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='volunteer_list',
            field=models.ManyToManyField(blank=True, related_name='volunteers', to=settings.AUTH_USER_MODEL),
        ),
    ]
