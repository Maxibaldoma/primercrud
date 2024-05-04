from django.shortcuts import render, redirect
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'compra/lista_productos.html', {'productos': productos})


def agregar_producto(request):
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compra:lista_productos')

    else:
        form = ProductoForm()
    return render(request, 'compra/agregar_producto.html', {'form': form, 'proveedores': proveedores})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all() # Obtener todos los proveedores de la base de datos
    # Renderizar la plantilla lista_proveedores.html con los proveedores
    return render(request, 'compra/lista_proveedores.html', {'proveedores': proveedores})


def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la lista de proveedores después de guardar correctamente
            return redirect('compra:lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'compra/agregar_proveedor.html', {'form': form})