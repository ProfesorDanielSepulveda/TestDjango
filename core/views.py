from django.shortcuts import render, redirect, get_object_or_404
from core.carrito import Carrito
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User


def home(request):
    request.session["version"]="2.2.3"
    servicios = Servicio.objects.all()
    context = {
        'version' : request.session["version"],     # Sesion
        'servicios': servicios, #servicios para slide
    }
    
    if "username" in request.session:
        context['usuario'] = request.session["username"]
    return render(request,'core\index.html',context)


def sobreNosotros(request):
    return render(request, 'core/sobreNosotros.html')

@login_required
@permission_required('auth.view_user')
def vista_admin(request):
    servicios = Servicio.objects.all()
    return render(request, 'core/vista_admin.html',{'servicios': servicios})

@login_required
def form_vehiculo(request):
    datos={
        'form': VehiculoForm()

    }

    #verificamos que peticion sean post y rescatamos los datos
    if request.method=='POST':
        formulario = VehiculoForm(request.POST)
         #verificar formulario
        if formulario.is_valid():
            #si es valido guardamos el formulario
            formulario.save()
            #mostrar un mensaje cuando se guarden los datos
            datos['mensaje'] = "Guardados correctamente"

    
    return render(request,'core/form_vehiculo.html',datos)

@login_required
@permission_required('auth.view_user')
def lista_vehiculo(request):
    vehiculos = Vehiculo.objects.all();
    
    for vehiculo in vehiculos:
        vehiculo.nombre_categoria = Categoria.objects.get(idCategoria=vehiculo.categoria_id).nombreCategoria

    return render (request, 'core/lista_vehiculo.html', {'vehiculos': vehiculos})

@login_required
@permission_required('auth.view_user')
def form_mod_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)

    datos = {
	    'form': VehiculoForm(instance=vehiculo)
	}

    if request.method =='POST':
        formulario = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Datos modificados'

    return render(request, 'core/form_mod_vehiculo.html', datos)

def inicio_sesion(request):
    return render(request,'core/inicio_sesion.html')



def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['contrasena']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if username == 'admin':
                    login(request, user)
                    return redirect('vista_admin')
                else:
                    login(request, user)
                    return redirect('index')
            else:
                form.add_error(None,'credenciales inválidas')
    else:
        form = LoginForm()
    
    return render(request, 'core/inicio_sesion.html', {'loginForm' : form})

def vistaLogeado(request):
    return render(request,'core/index.html')


def cerrar_sesion(request):
    auth_logout(request)
    if 'username' in request.session:
        del request.session['username']  
    
    return redirect('home') 

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'core/servicios.html', {'servicios':servicios})

def agregar_servicio(request, idServicio):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(idServicio=idServicio)
    carrito.agregar(servicio)
    return redirect("servicios")

def eliminar_servicio(request, idServicio):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(idServicio=idServicio)
    carrito.eliminar(servicio)
    return redirect("servicios")

def restar_servicio(request, idServicio):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(idServicio=idServicio)
    carrito.restar(servicio)
    return redirect("servicios")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("servicios")

@login_required
@permission_required('auth.view_user')
def agregar_servicio_admin(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vistaAdminProductos')
    else:
        # Si no es una solicitud POST, crea un formulario vacío de Producto
        form = ServicioForm()
    # Renderiza la plantilla 'agregar_producto.html' y pasa el formulario como contexto
    return render(request, 'core/agregar_producto.html', {'form': form})

def registrarse(request):
    data = {
        'form': SigninForm() 
    }
    
    if request.method == 'POST':
        user_creation_form = SigninForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
    
    return render(request, 'core/registro.html',data)

@login_required
@permission_required('auth.view_user')
def form_categoria(request):
    datos= {
        'form': CategoriaForm()
    }
    if request.method=='POST':  
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Categoria ingresada correctamente.'
    
    return render(request,'core/form_categoria.html',datos)

@login_required
@permission_required('auth.view_user')
def lista_categoria(request):
    categorias = Categoria.objects.all();

    return render(request, 'core/lista_categoria.html', {'categorias': categorias})

@login_required
@permission_required('auth.view_user')
def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="lista_vehiculo")

@login_required
@permission_required('auth.view_user')
def form_mod_categoria(request,id):
    categoria = Categoria.objects.get(idCategoria=id)

    datos = {
	    'form': CategoriaForm(instance=categoria)
	}

    if request.method =='POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Datos modificados'

    return render(request, 'core/form_mod_categoria.html', datos)

@login_required
@permission_required('auth.view_user')
def form_del_categoria(request,id):
    categoria = Categoria.objects.get(idCategoria=id)
    categoria.delete()
    return redirect(to="lista_categoria")

@login_required
@permission_required('auth.view_user')
def lista_servicios(request):
    servicios = Servicio.objects.all();

    return render(request, 'core/lista_servicios.html', {'servicios': servicios})

@login_required
@permission_required('auth.view_user')
def form_servicios(request):
    datos= {
        'form': ServicioForm()
    }
    if request.method=='POST':  
        formulario = ServicioForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Servicio ingresado correctamente.'
    
    return render(request,'core/form_servicios.html',datos)

def contacto(request):
    datos= {
        'form': MensajeForm()
    }
    if request.method=='POST':  
        formulario = MensajeForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Se ha enviado el mensaje correctamente. Un mecánico se pondrá en contacto contigo en breve.'
    
    return render(request,'core/contacto.html',datos)

@login_required
@permission_required('auth.view_user')
def lista_mensajes(request):
    mensajes = Mensaje.objects.all();

    return render(request, 'core/lista_mensajes.html', {'mensajes': mensajes})

@login_required
@permission_required('auth.view_user')
def form_del_mensaje(request,id):
    mensaje = Mensaje.objects.get(idCarta=id)
    mensaje.delete()
    return redirect(to="lista_mensajes")

@login_required
@permission_required('auth.view_user')
def lista_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'core/lista_mecanicos.html', {'mecanicos': mecanicos})

@login_required
@permission_required('auth.view_user')
def form_mecanicos(request):
    datos= {
        'form': MecanicoForm()
    }
    if request.method=='POST':  
        formulario = MecanicoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Mécanico ingresado correctamente.'
    
    return render(request,'core/form_mecanicos.html',datos)

@login_required
@permission_required('auth.view_user')
def form_mod_servicio(request,id):
    servicio = get_object_or_404(Servicio, idServicio=id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm(instance=servicio)
        
    return render(request, 'core/form_mod_servicios.html', {'form': form, 'servicio': servicio})


@login_required
@permission_required('auth.view_user')
def form_del_servicio(request,id):
    servicio = Servicio.objects.get(idServicio=id)
    servicio.delete()
    return redirect(to="lista_servicios")

@login_required
@permission_required('auth.view_user')
def form_mod_mecanico(request,id):
    mecanicos = get_object_or_404(Mecanico, idMecanico=id)
    if request.method == 'POST':
        form = MecanicoForm(request.POST, request.FILES, instance=mecanicos)
        if form.is_valid():
            form.save()
            return redirect('lista_mecanicos')
    else:
        form = MecanicoForm(instance=mecanicos)
        
    return render(request, 'core/form_mod_mecanicos.html', {'form': form, 'servicio': mecanicos})

@login_required
@permission_required('auth.view_user')
def form_del_mecanico(request,id):
    mecanico = Mecanico.objects.get(idMecanico=id)
    mecanico.delete()
    return redirect(to="lista_mecanicos")


def nuestros_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'core/mecanicos.html', {'mecanicos': mecanicos})


@login_required
def guardar_compra(request):
    if request.method == "POST":
        
        compra = Compra(precio_total=0)
        compra.save()
        
        carrito = Carrito(request)

        for key, values in carrito.carrito.items():
            servicio_id = values["idServicio"]
            cantidad = values["cantidad"]
            precio = values["acumulado"]
            
            detalle_compra = Detalle_compra(
                servicio_id=servicio_id,
                compra=compra,
                cantidad_producto=cantidad,
                precio_total=precio
            )
            detalle_compra.save()

        # Actualiza el Precio_total de la Compra
        compra.precio_total = sum(item["acumulado"] for item in carrito.carrito.values())
        compra.save()

        # Limpia el carrito de compras después de realizar la compra
        carrito.limpiar()

        # Redirecciona a una página de confirmación o a otra vista
        return render(request, "core/index.html")

    return render(request, "core/lista_venta.html")

@login_required
@permission_required('auth.view_user')
def vistaAdminVentas(request):
    compra = Compra.objects.all().order_by('-id_compra')

    det_compra = Detalle_compra.objects.all()

    datos = {
        'compra': compra,
        'det_compra':det_compra
    }
    return render(request, 'core/lista_ventas_admin.html', {**datos})

@login_required
@permission_required('auth.view_user')
def detalle_venta(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra) 
    det_compra = Detalle_compra.objects.filter(compra_id=compra.id_compra).order_by('-id') 
    
    id_compra_prueba = id_compra
    totalCompra = compra.precio_total

    datos = {
        'compra': [compra], 
        'det_compra': det_compra,
        'id_compra_prueba': id_compra_prueba,
        'totalCompra': totalCompra
    }
    return render(request, 'core/venta_detalle.html', datos)

@login_required
@permission_required('auth.view_user')
def eliminar_venta(request, id_compra):
    compra = get_object_or_404(Compra, id_compra=id_compra)
    if request.method == 'POST':
        compra.delete()
        return redirect('lista_ventas_admin')
    
    return render(request, 'core/compra_eliminar.html', {'compra': compra})
