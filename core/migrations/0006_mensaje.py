# Generated by Django 4.1.5 on 2023-06-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_servicio_descripcionservicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('idCarta', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=15, null=True, verbose_name='Rut')),
                ('pasaporte', models.CharField(max_length=12, null=True, verbose_name='Pasaporte')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('ap_paterno', models.CharField(max_length=50, verbose_name='Apellido paterno:')),
                ('ap_materno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('sexo', models.CharField(max_length=50, verbose_name='Sexo')),
                ('celular', models.IntegerField(verbose_name='Celular')),
                ('mensaje', models.CharField(max_length=500, verbose_name='Mensaje')),
            ],
        ),
    ]