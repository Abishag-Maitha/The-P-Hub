# Generated by Django 4.0.5 on 2022-06-11 20:32

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='projectscreenshot',
            new_name='projectimage',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Bio',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='images'),
        ),
    ]
