# Generated by Django 4.1 on 2022-09-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeloRelacionalBaseDeDatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='fecha_creacion',
            field=models.DateField(auto_now=True),
        ),
    ]
