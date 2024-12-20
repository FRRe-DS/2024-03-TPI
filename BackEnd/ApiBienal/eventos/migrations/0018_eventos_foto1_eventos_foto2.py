# Generated by Django 5.1.1 on 2024-11-16 03:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0017_profile_activation_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='foto1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='res.cloudinary.com/dq1vfo4c8/image'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='foto2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='res.cloudinary.com/dq1vfo4c8/image'),
        ),
    ]
