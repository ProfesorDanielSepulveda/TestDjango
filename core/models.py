from django.db import models
from django.forms import ModelForm


# Create your models here.

#Modelo para categoria

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

#Modelado para el vehiculo

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca vehiculo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
    

class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True, verbose_name= "Id Servicio")
    nombreServicio = models.CharField(max_length=50, verbose_name="Nombre Servicio")
    precioServicio = models.IntegerField(verbose_name="Precio Servicio")
    descripcionServicio = models.CharField(max_length=500, verbose_name="Descripcion Servicio")
    imagenServicio = models.ImageField(upload_to='servicios', verbose_name="Imagen del servicio")

    def __str__(self):
        return self.nombreServicio
    
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, verbose_name="Id Cliente")
    correoCliente = models.CharField(unique=True, max_length=50, verbose_name="Correo")
    contrasenaCliente = models.CharField(max_length=50, verbose_name="Contraseña")
    runCliente = models.CharField(unique=True, max_length=12, verbose_name="Run")
    nombresCliente = models.CharField(max_length=100, verbose_name="Nombres")
    apPaternoCliente = models.CharField(max_length=50, verbose_name="Apellido Paterno")
    apMaternoCliente = models.CharField(max_length=50, verbose_name="Apellido Materno ")
    direccionCliente = models.CharField(max_length=100, verbose_name="Direccion")
    telefonoCliente = models.IntegerField(verbose_name="Telefono")

    def __str__(self):
        return self.runCliente
    
class Mecanico(models.Model):
    idMecanico = models.AutoField(primary_key=True, verbose_name="Id Mecanico")
    runMecanico = models.CharField(unique=True, max_length=12, verbose_name="Run Mecanico")
    nombresMecanico = models.CharField(max_length=100, verbose_name="Nombres Mecanico")
    apPaternoMecanico = models.CharField(max_length=50, verbose_name="Ap Paterno Mecanico")
    apMaternoMecanico = models.CharField(max_length=50, verbose_name="Ap Materno Mecanico")
    direccionMecanico = models.CharField(max_length=100, verbose_name="Direccion Mecanico")
    telefonoMecanico = models.IntegerField(verbose_name="Telefono Mecanico")
    correoMecanico = models.CharField(max_length=50, verbose_name="Correo Mecanico")
    descripcionMecanico = models.CharField(max_length=500, verbose_name="Descripcion de mecanico")
    sueldoMecanico = models.IntegerField(verbose_name="Sueldo Mecanico")
    imagenMecanico = models.ImageField(upload_to='mecanicos', verbose_name="Imagen del mecanico",default='core/img/logobueno.png')
    trabajosRealizados = models.IntegerField(verbose_name="Trabajos realizados",)

    def __str__(self):
        return self.runMecanico

class Usuario(models.Model):
    rut = models.CharField(max_length=12,verbose_name='Rut')
    username = models.CharField(max_length=50,verbose_name='Nombre Usuario')
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    apellido = models.CharField(max_length=50,verbose_name='Apellido')
    contrasena = models.CharField(max_length=50,verbose_name='Contraseña')
    direccion = models.CharField(max_length=80,verbose_name='Direccion')
    email = models.EmailField(unique=True,verbose_name="Correo electrónico")

    def __str__(self):
        return self.username
    
class Mensaje(models.Model):
    idCarta = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=15, verbose_name='Rut',null=True,blank=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    ap_paterno = models.CharField(max_length=50,verbose_name='Apellido paterno:')
    ap_materno = models.CharField(max_length=50,verbose_name='Apellido materno')
    sexo = models.CharField(max_length=50,verbose_name='Sexo')
    celular = models.IntegerField(verbose_name='Celular')
    mensaje = models.CharField(max_length=500,verbose_name='Mensaje')
    
    def __str__(self):
        return self.nombre

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True, verbose_name='id Compra')
    precio_total = models.IntegerField(verbose_name='precio Total')

    def __str__(self):
        return str(self.id_compra)

class Detalle_compra(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField(verbose_name='Cantidad Productos')
    precio_total = models.IntegerField(verbose_name='Precio Total')

    def __str__(self):
        return f"Detalle {self.id}"
    