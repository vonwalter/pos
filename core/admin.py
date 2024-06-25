from django.contrib import admin
from .models import Empresa, PuntoDeVenta, Cliente, Producto, Stock, Compra, DetalleCompra, Venta, DetalleVenta

admin.site.register(Empresa)
admin.site.register(PuntoDeVenta)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Stock)
admin.site.register(Compra)
admin.site.register(DetalleCompra)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
