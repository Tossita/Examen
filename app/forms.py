from django import forms
from django.forms import ModelForm
from.models import Carrito, Producto
from.models import Cliente
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=3,max_length=20)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','descripcion','tipo','stock', 'imagen']

    #widgets = {
           # 'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
      #  }

class ClienteForm(ModelForm):

    nombre = forms.CharField(min_length=3,max_length=20)
    apellido = forms.CharField(min_length=4,max_length=20)
    clave = forms.CharField(label="Clave", widget=forms.PasswordInput, strip=False)

    

    class Meta:
        model = Cliente
        fields = ['run','nombre','apellido','clave','correo','region','comuna', 'direccion', 'tipo', 'imagen']
    

class UserRegistroForm(UserCreationForm):
	
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class SeguimientoForm(ModelForm):
	


    class Meta:
        model = Seguimiento
        fields = ['estado']