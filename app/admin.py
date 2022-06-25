from django.contrib import admin
from .models import *

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','descripcion','tipo','stock', 'imagen', 'created_at', 'updated_at']
    search_fields =['codigo']
    list_per_page = 5

class ClientesAdmin(admin.ModelAdmin):
    list_display = ['run','nombre','apellido','clave','correo','region', 'comuna', 'direccion', 'tipo', 'imagen', 'created_at', 'updated_at']
    search_fields =['run']
    list_per_page = 5


class CarritoAdmin(admin.ModelAdmin):
    list_display = ['cod_carrito','producto','cantidad','total', 'num_carrito', 'comprado']
    search_fields =['cod_carrito']
    list_per_page = 5

class EstadoAdmin(admin.ModelAdmin):
    list_display = ['num_seguimiento','estado']
    search_fields =['num_seguimiento']
    list_per_page = 5


class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ['user','suscrito']
    search_fields =['']
    list_per_page = 5


class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ['cod_seguimiento','estado', 'user', 'num_carrito', 'created_at', 'updated_at']
    search_fields =['cod_seguimiento']
    list_per_page = 5



admin.site.register(TipoProducto)
admin.site.register(TipoPago)
admin.site.register(TipoCliente)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Seguimiento, SeguimientoAdmin)

