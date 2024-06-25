from django.shortcuts import render, get_object_or_404, redirect
from .models import Empresa, PuntoDeVenta, Cliente, Producto, Compra, Venta
from .forms import EmpresaForm, PuntoDeVentaForm, ClienteForm, ProductoForm, CompraForm, VentaForm

def home(request):
    return render(request, 'core/home.html')

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from .models import Empresa, Usuario

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            empresa = form.cleaned_data.get('empresa')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.empresa == empresa:
                    auth_login(request, user)
                    request.session['empresa_id'] = empresa.id
                    request.session['sucursal_id'] = user.sucursal.id if user.sucursal else None
                    request.session['rol'] = user.rol
                    return redirect('home')
                else:
                    form.add_error('empresa', 'Empresa incorrecta para este usuario.')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def home(request):
    empresa_id = request.session.get('empresa_id')
    sucursal_id = request.session.get('sucursal_id')
    rol = request.session.get('rol')
    return render(request, 'core/home.html', {'empresa_id': empresa_id, 'sucursal_id': sucursal_id, 'rol': rol})

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'core/lista_empresas.html', {'empresas': empresas})

def detalle_empresa(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    return render(request, 'core/detalle_empresa.html', {'empresa': empresa})

def crear_empresa(request):
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save()
            return redirect('detalle_empresa', pk=empresa.pk)
    else:
        form = EmpresaForm()
    return render(request, 'core/crear_empresa.html', {'form': form})

# Vistas para Sucursales (Puntos de Venta)
def lista_puntos_venta(request):
    puntos_venta = PuntoDeVenta.objects.all()
    return render(request, 'core/lista_puntos_venta.html', {'puntos_venta': puntos_venta})

def detalle_punto_venta(request, pk):
    punto_venta = get_object_or_404(PuntoDeVenta, pk=pk)
    return render(request, 'core/detalle_punto_venta.html', {'punto_venta': punto_venta})

def crear_punto_venta(request):
    if request.method == "POST":
        form = PuntoDeVentaForm(request.POST)
        if form.is_valid():
            punto_venta = form.save()
            return redirect('detalle_punto_venta', pk=punto_venta.pk)
    else:
        form = PuntoDeVentaForm()
    return render(request, 'core/crear_punto_venta.html', {'form': form})

# Vistas para Clientes
def seleccionar_empresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'core/seleccionar_empresa.html', {'empresas': empresas})


def lista_clientes(request, empresa_pk):
    empresa = get_object_or_404(Empresa, pk=empresa_pk)
    clientes = Cliente.objects.filter(empresa=empresa)
    return render(request, 'core/lista_clientes.html', {'empresa': empresa, 'clientes': clientes})

def detalle_cliente(request, empresa_pk, cliente_pk):
    cliente = get_object_or_404(Cliente, pk=cliente_pk, empresa_id=empresa_pk)
    return render(request, 'core/detalle_cliente.html', {'cliente': cliente})

def crear_cliente(request, empresa_pk):
    empresa = get_object_or_404(Empresa, pk=empresa_pk)
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.empresa = empresa
            cliente.save()
            return redirect('detalle_cliente', empresa_pk=empresa.pk, cliente_pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'core/crear_cliente.html', {'form': form, 'empresa': empresa})