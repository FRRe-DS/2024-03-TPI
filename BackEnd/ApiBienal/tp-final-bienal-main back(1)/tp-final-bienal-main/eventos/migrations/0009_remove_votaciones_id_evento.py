# Generated by Django 5.1.1 on 2024-09-26 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0008_remove_escultores_foto_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votaciones',
            name='id_evento',
        ),
    ]