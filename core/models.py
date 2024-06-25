# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class PuntoDeVenta(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    ROLES = [
        ('vendedor', 'Vendedor'),
        ('gerente', 'Gerente'),
        ('secretario', 'Secretario'),
    ]
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    sucursal = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE, null=True, blank=True)
    rol = models.CharField(max_length=20, choices=ROLES)

class Cliente(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    cuit = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    punto_venta = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
    proveedor = models.CharField(max_length=255)
    numero_factura = models.CharField(max_length=13)  # formato 0000-00000000
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.numero_factura} - {self.proveedor}"

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    numero_factura = models.CharField(max_length=15)
    productos = models.ManyToManyField(Producto)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    punto_venta = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.numero_factura} - {self.cliente.nombre}"

class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='stock_entries')
    cantidad = models.IntegerField()
    fecha = models.DateField()
    punto_venta = models.ForeignKey(PuntoDeVenta, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.producto.nombre} - {self.punto_venta.nombre}- {self.cantidad} unidades"
    
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.compra.numero_factura}"
    
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} - {self.venta.numero_factura}"