from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="indexPrin"),
    path('index/', indexU, name="index"),
    path('carrito/', carritoCompras, name="carritoCompras"),
    path('historial/', historial, name="historial"),
    path('registro/', registro, name="registro"),
    path('seguimiento/', seguimiento, name="seguimiento"),
    path('seguimientoAdmin/', seguimientoAdmin, name="seguimientoAdmin"),
    path('suscripcion/', suscripcion, name="suscripcion"),
    path('usuario/', usuario, name="usuario"),
    path('compra_exitosa/', compra_exitosa, name="compra_exitosa"),
    path('productos/', ventas, name="ventas"),
    path('base/', base, name="base"),
    path('ventas/', ventasDos, name="ventasDos"),
    path('ventas_api/', ventas_api, name="ventas_api"),
    path('indexPrueba/', indexPrueba, name="indexPrueba"),
    path('onprocess/', onprocess, name="onprocess"),
    path('agregar/', agregar_producto, name="agregar_producto"),
    path('base2/', base2, name="base2"),
    path('listar_prod/', listar_productos, name="listar_productos"),
    path('listar_user/', listar_usuarios, name="listar_usuarios"),
    path('modificar_prod/<codigo>', modificar_producto, name="modificar_producto"),
    path('modificar_user/<run>', modificar_usuarios, name="modificar_usuarios"),
    path('modificar_seguimiento/<cod_seguimiento>', modificar_seguimiento, name="modificar_seguimiento"),
    path('eliminar_prod/<codigo>', eliminar_producto, name="eliminar_producto"),
    path('eliminar_user/<run>', eliminar_usuarios, name="eliminar_usuarios"),
    path('perfil/', perfil, name="perfil"),
    path('registro_usuarios/', registro_usuarios, name="registro_usuarios"),

    
]

