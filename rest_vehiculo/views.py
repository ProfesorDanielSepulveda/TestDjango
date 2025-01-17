from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Vehiculo
from .serializers import VehiculoSerializer
from rest_framework import viewsets
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('auth.view_user')
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_vehiculos(request):
    if request.method == 'GET':
        vehiculo = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@login_required
@permission_required('auth.view_user')
@api_view(['GET', 'PUT','DELETE'])
def detalle_vehiculo(request, id):
    try:
        vehiculo = Vehiculo.objects.get(patente=id)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(vehiculo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer