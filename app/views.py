from ast import Global
from tkinter.tix import MAX
import requests #permite leer el api
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from distutils.log import debug
from itertools import product
from tracemalloc import stop
from.models import *
from.forms import *
from app.forms import ProductoForm
from app.forms import ClienteForm




# Create your views here.




def index(request):
    return render(request, 'app/index.html')

@login_required
def perfil(request):
    num_visitas = request.session.get('num_visitas', 0)
    request.session['num_visitas'] = num_visitas + 1
    request.session.set_expiry(30)
    datos = {'visitas' : num_visitas}
    return render(request, 'app/perfil.html', datos)

@login_required
def indexU (request):
    return render(request, 'app/indexUsuario.html')

#def carrito (request):
   # return render(request, 'app/carritoCompras.html')

@login_required
def historial (request):
    return render(request, 'app/historial.html')

def registro (request):
    datos = {
        'form' : ClienteForm()
    }
    if request.method == 'POST' :
        formulario = ClienteForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos ['mensaje'] = 'Cliente guardado correctamente!'

    return render(request, 'app/registro.html', datos)


#Segimiento del usuario y del admin
@login_required
def seguimiento (request):


    

    return render(request, 'app/seguimiento.html')


@login_required
def seguimientoAdmin (request):

    seguimientoAll = Seguimiento.objects.all()

    

    datos = {
        'listarSeguimientos' : seguimientoAll,
    }



    return render(request, 'app/seguimientoAdmin.html',datos)

@login_required
def suscripcion (request):
    mensaje=''
    if request.method == 'POST' :
        opcion = request.POST.get('suscrito')

        if opcion=='True':
            suscripcion=Suscripcion()
            suscripcion.user=request.user
            suscripcion.suscrito=True
            mensaje='suscripcion exitosa'
            suscripcion.save()
        elif opcion=='False':
            suscripcion = Suscripcion.objects.get(user=request.user)
            suscripcion.delete()
            mensaje='desuscripcion exitosa'


    datos = {
        'dato' : mensaje
    }

    return render(request, 'app/suscripcion.html', datos)



@login_required
def usuario(request):
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll
    }
    return render(request, 'app/usuario.html', datos)

@login_required
def listar_usuarios(request):
    clienteAll = Cliente.objects.all()
    datos = {
        'listarClientes' : clienteAll
    }
    return render(request, 'app/listar_usuarios.html', datos)

#def usuario (request):
#   return render(request, 'app/usuario.html')

@login_required
def ventas (request):
    return render(request, 'app/ventas.html')

@login_required
def compra_exitosa (request):
    
    carrito = Carrito.objects.filter(user = request.user, comprado = False)
    for x in carrito:
        producto = Producto.objects.get(codigo=x.producto.codigo)
        producto.stock-=1
        producto.save()

    seguimiento=Seguimiento.objects.get(num_carrito=carrito[0].num_carrito)

    seguimiento.estado = 'Validación'

    seguimiento.save()

    for x in carrito:
        x.comprado = True 
        x.save()
    
    
    return render(request, 'app/compra_exitosa.html')

def base(request):
    return render(request, 'app/base.html')
   


def indexPrueba(request):
    return render(request, 'app/indexPrueba.html')

#elimnar
def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_productos")

def eliminar_usuarios(request, run):
    usuario = Cliente.objects.get(run=run)
    usuario.delete()

    return redirect(to="listar_usuarios")


def onprocess(request):
    return render(request, 'app/status_onprocess.html')


#seccion agregar
@permission_required('app.add_producto')
def agregar_producto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST , files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
            

    return render(request, 'app/productos/agregar_producto.html', datos)
   

#seccion listar
@login_required
def ventasDos(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll,
        'listaJson': response
    }
    if request.method == 'POST' :
        
        tipo = TipoProducto()
        tipo.tipo = request.POST.get('tipo')

        producto = Producto()
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.descripcion = request.POST.get('descripcion')
        producto.stock = request.POST.get('stock')
        producto.tipo = tipo
        producto.imagen = request.POST.get('imagen')

        if len(Carrito.objects.filter(user=request.user, comprado = False))== 0:
            carritonuevo = Carrito() 
            carritonuevo.user = request.user
            carritonuevo.producto = producto
            carritonuevo.cantidad = 0
            carritonuevo.comprado = False
            carritonuevo.save()

            carritonuevo.num_carrito = carritonuevo.cod_carrito
            carritonuevo.save()
        else:
            carritos = Carrito.objects.filter(user=request.user, comprado = False)
            carritonuevo = Carrito() 
            carritonuevo.num_carrito = carritos[0].cod_carrito
            carritonuevo.user = request.user
            carritonuevo.producto = producto
            carritonuevo.cantidad = 0
            carritonuevo.comprado = False
        
        carritonuevo.save()

        seguimiento = Seguimiento.objects.filter(user = request.user)
        
        cod_seg = 0
        num_carrito = carritonuevo.num_carrito
        exist_seg = False

        for x in seguimiento:
            num_seg_carr = x.num_carrito
            if num_seg_carr == num_carrito :
                cod_seg = x.cod_seguimiento
                exist_seg = True
            
        if exist_seg == True:
            seguimiento_actual = Seguimiento.objects.get(cod_seguimiento=cod_seg)
            seguimiento_actual.estado = 'No comprado'
            seguimiento_actual.save()
        else:
            seguimiento_actual = Seguimiento()
            seguimiento_actual.num_carrito = num_carrito
            seguimiento_actual.user = request.user
            seguimiento_actual.estado = 'No comprado'
            seguimiento_actual.save()

    return render(request, 'app/ventasDos.html', datos)



def ventas_api(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()
    response2 = requests.get('https://spapi.dev/api/characters').json()
    response3 = requests.get('https://rickandmortyapi.com/api/character').json()
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll,
        'listaJson': response,
        'listaSP': response2,
        'listaRandM': response3 ['results'],
    }
    if request.method == 'POST' :
        tipo = TipoProducto()
        tipo.tipo = request.POST.get('tipo')

        producto = Producto()
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.precio = request.POST.get('precio')
        producto.descripcion = request.POST.get('descripcion')
        producto.stock = request.POST.get('stock')
        producto.tipo = tipo
        producto.imagen = request.POST.get('imagen')

        carrito = Carrito()
        carrito.producto = producto
        carrito.cantidad = 0
        carrito.save()



    return render(request, 'app/ventas_api.html', datos)



def base2(request):
    return render(request, 'app/base2.html')

#modificar
def modificar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos ['mensaje'] = 'Producto modificado correctamente!'
            datos ['form'] = formulario

    return render(request, 'app/productos/modificar_producto.html', datos)


def modificar_usuarios(request, run):
    usuario = Cliente.objects.get(run=run)
    datos = {
        'form' : ClienteForm(instance=usuario)
    }
    if request.method == 'POST' :
        formulario = ClienteForm(request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos ['mensaje'] = 'Cliente modificado correctamente!'
            datos ['form'] = formulario

    return render(request, 'app/modificar_usuarios.html', datos)


def modificar_seguimiento(request, cod_seguimiento):
    estados = ['No comprado','Validación', 'Preparación', 'Reparto', 'Entregado']
    seguimiento = Seguimiento.objects.get(cod_seguimiento=cod_seguimiento)
    
    if request.method == 'POST' :
        formulario = SeguimientoForm(request.POST, files=request.FILES, instance=seguimiento)
        estado = request.POST.get('estado')
        seguimiento.estado = estado
        seguimiento.save()

    datos = {
        'form' : SeguimientoForm(instance=seguimiento),
        'seguimiento' : seguimiento,
        'estados' : estados

    }



    return render(request, 'app/modificar_seguimiento.html', datos)


#listar

def listar_productos(request):
    productoAll = Producto.objects.all()
    datos = {
        'listarProductos' : productoAll
    }

    
    return render(request, 'app/productos/listar_productos.html', datos)


def modificar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos ['mensaje'] = 'Producto modificado correctamente!'
            datos ['form'] = formulario

    return render(request, 'app/productos/modificar_producto.html', datos)


def carritoCompras(request):
    if request.method == 'POST' :
        sacarProducto = request.POST.get('sacarProducto')
        codigoProducto = request.POST.get('prod')
        
        prod=Producto.objects.get(codigo = codigoProducto)

        mydata = Carrito.objects.filter(producto=prod, user = request.user, comprado = False )
        mydata[0].delete()

    carrito = Carrito.objects.filter(user = request.user, comprado = False )

    listaCarrito = []
    listaCodigo = []
    total = 0
    subtotal=0
    descuento =0
    

    for x in carrito:
        
    	if x.producto.codigo not in listaCodigo:
            listaCarrito.append(x)
            listaCodigo.append(x.producto.codigo)

    for x in listaCarrito:
        for y in carrito:
            if x.producto.codigo == y.producto.codigo:
                x.cantidad += 1

    for x in listaCarrito:
        cantidad_pro = x.cantidad
        precio_pro = x.producto.precio
        total_por_producto = cantidad_pro*precio_pro
        subtotal+=total_por_producto
    descuento = 0
    try:
        suscripcion = Suscripcion.objects.get(user=request.user)

        if suscripcion.suscrito :
            descuento = round(subtotal*0.05)
        else:
            descuento = 0
    except:
        descuento = 0

    
    total = subtotal-descuento
    datos = {
        'listaCarrito' : listaCarrito,

        'subtotal': subtotal,
        'descuento': descuento,
        'total': total,
    }

    

    


    

    return render(request, 'app/carritoCompras.html', datos)


def registro_usuarios(request):
    datos = {
        'form' : UserRegistroForm()
    }
    if request.method == 'POST':
        formulario = UserRegistroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario
    return render(request, 'registration/registro_usuarios.html', datos)



    

#def searchbar(request):
#    if request.method == 'GET':
#       search = request.GET.get('search')
#       producto = Producto.objects.all().filter(producto=search)
#       producto = Producto.objects.get(producto = search)
#       posts = producto.posts.all()
#       return render(request, 'ventasDos.html', {'producto': producto, 'posts': posts})