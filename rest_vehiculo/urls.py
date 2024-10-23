from django.urls import path, include
from rest_vehiculo.views import *
from rest_framework import routers
from rest_vehiculo.viewslogin import login

router = routers.DefaultRouter()
router.register(r'vehiculos',VehiculoViewSet)

urlpatterns = [
    path('lista_vehiculos', lista_vehiculos, name="lista_vehiculos"),
    path('detalle_vehiculo/<id>', detalle_vehiculo, name="detalle_vehiculo"),
    path('', include(router.urls)),
    path('login', login, name="login")
]


