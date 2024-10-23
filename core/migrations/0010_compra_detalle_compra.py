# Generated by Django 4.1.5 on 2023-07-12 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_modelo_marca_delete_marca_delete_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False, verbose_name='id Compra')),
                ('precio_total', models.IntegerField(verbose_name='precio Total')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField(verbose_name='Cantidad Productos')),
                ('precio_total', models.IntegerField(verbose_name='Precio Total')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compra')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servicio')),
            ],
        ),
    ]
