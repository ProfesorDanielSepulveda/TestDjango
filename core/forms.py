from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#creamos nuestra clase para el formulario desde la base de datos
class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']

class ClienteForm(ModelForm)   :

    class Meta:
        model = Cliente
        fields = ['correoCliente', 'contrasenaCliente', 'runCliente', 'nombresCliente', 'apPaternoCliente', 'apMaternoCliente', 'direccionCliente', 'telefonoCliente']

class LoginForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'contrasena']
        
class ServicioForm(ModelForm):
        class Meta:
            model = Servicio
            fields = ['nombreServicio', 'precioServicio', 'descripcionServicio', 'imagenServicio']
        
class SigninForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirme contraseña'
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut',
                  'username',
                  'nombre',
                  'contrasena',
                  'direccion',
                  'email',
                  ]
        

class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria']
        
class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = ['idCarta',
                  'rut',
                  'nombre',
                  'ap_paterno',
                  'ap_materno',
                  'sexo',
                  'celular',
                  'mensaje']
        
class MecanicoForm(ModelForm):
    class Meta:
        model = Mecanico
        fields = ['runMecanico',
                  'nombresMecanico',
                  'apPaternoMecanico',
                  'apMaternoMecanico',
                  'direccionMecanico',
                  'telefonoMecanico',
                  'correoMecanico',
                  'descripcionMecanico',
                  'sueldoMecanico',
                  'imagenMecanico',
                  'trabajosRealizados']