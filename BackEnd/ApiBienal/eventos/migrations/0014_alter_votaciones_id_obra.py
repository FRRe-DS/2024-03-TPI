# Generated by Django 5.1.1 on 2024-09-30 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0013_alter_escultores_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votaciones',
            name='id_obra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.obras'),
        ),
    ]