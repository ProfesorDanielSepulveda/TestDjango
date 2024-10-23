from django.contrib import admin
from .models import *
# Register your models here.
# Agregar modelos acá permite administrarlos desde
# el panel de Django

admin.site.register(Categoria)
admin.site.register(Mecanico)
admin.site.register(Servicio)
admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Mensaje)
admin.site.register(Compra)
admin.site.register(Detalle_compra)
