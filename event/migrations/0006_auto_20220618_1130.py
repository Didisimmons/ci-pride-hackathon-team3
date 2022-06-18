# Generated by Django 3.2 on 2022-06-18 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0005_alter_donation_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(default='default.jpg', upload_to='event_featured_images'),
        ),
        migrations.AddField(
            model_name='event',
            name='volunteer_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='volunteers', to=settings.AUTH_USER_MODEL),
        ),
    ]