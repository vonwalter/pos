from django import forms
from .models import Empresa, PuntoDeVenta, Cliente, Producto, Compra, Venta, Usuario

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'empresa', 'sucursal', 'rol']

class LoginForm(AuthenticationForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), required=True)

    class Meta:
        model = Usuario
        fields = ['username', 'password', 'empresa']

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'direccion', 'telefono', 'email']

class PuntoDeVentaForm(forms.ModelForm):
    class Meta:
        model = PuntoDeVenta
        fields = ['empresa', 'nombre', 'direccion', 'telefono']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email', 'cuit']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['punto_venta', 'proveedor', 'numero_factura', 'total']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['punto_venta', 'usuario', 'cliente', 'numero_factura', 'total']
