# Generated by Django 3.0.3 on 2020-04-02 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='registro_id',
        ),
        migrations.DeleteModel(
            name='Registros',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
