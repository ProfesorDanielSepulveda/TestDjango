from django.contrib import admin
from django.urls import path
from core import views
from .views import *
from django.urls import path


urlpatterns = [
    path('',home, name="home"),
    path('sobreNosotros',sobreNosotros, name="sobreNosotros"),
    path('login/', loginView, name='login'),
    path('accounts/login/',loginView,name='login'),
    path('index',vistaLogeado,name="index"),
    path('accounts/logout/',cerrar_sesion,name='logout'),
    path('servicios',servicios,name='servicios'),
    path('agregar/<idServicio>/', agregar_servicio,name="Add"),
    path('eliminar/<idServicio>/', eliminar_servicio,name="Del"),
    path('restar/<idServicio>/', restar_servicio,name="Sub"),
    path('limpiar/', limpiar_carrito,name="CLS"),
    path('registro', registrarse,name="registro"),
    path('form_vehiculo',form_vehiculo,name="form_vehiculo"),
    path('lista_vehiculo',lista_vehiculo,name="lista_vehiculo"),
    path('form_mod_vehiculo/<id>',form_mod_vehiculo,name="form_mod_vehiculo"),
    path('form_del_vehiculo/<id>',form_del_vehiculo, name="form_del_vehiculo"),
    path('form_categoria',form_categoria,name="form_categoria"),
    path('lista_categoria',lista_categoria,name="lista_categoria"),
    path('form_mod_categoria/<id>',form_mod_categoria,name="form_mod_categoria"),
    path('form_del_categoria/<id>',form_del_categoria,name="form_del_categoria"),
    path('lista_servicios',lista_servicios,name="lista_servicios"),
    path('form_servicios',form_servicios,name="form_servicios"),
    path('form_mod_servicios/<id>',form_mod_servicio,name="form_mod_servicios"),
    path('form_del_servicios/<id>',form_del_servicio,name="form_del_servicios"),
    path('vista_admin',vista_admin,name="vista_admin"),
    path('contacto',contacto,name="contacto"),
    path('lista_mensajes',lista_mensajes,name="lista_mensajes"),
    path('form_del_mensaje/<id>',form_del_mensaje,name="form_del_mensaje"),
    path('lista_mecanicos',lista_mecanicos,name="lista_mecanicos"),
    path('form_mecanicos',form_mecanicos,name="form_mecanicos"),
    path('form_mod_mecanico/<id>',form_mod_mecanico,name="form_mod_mecanico"),
    path('form_del_mecanico/<id>',form_del_mecanico,name="form_del_mecanico"),
    path('nuestros_mecanicos',nuestros_mecanicos,name="nuestros_mecanicos"),
    path('guardar_compra', guardar_compra, name='guardar_compra'),
    path('lista_ventas_admin',vistaAdminVentas,name="lista_ventas_admin"),
    path('detalle/<int:id_compra>/', detalle_venta, name='detalle_venta'),
    path('eliminar_venta/<int:id_compra>/', eliminar_venta, name='eliminar_venta'),
    
]
