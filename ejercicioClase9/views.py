from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponse, JsonResponse
import json

# READ

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


# CREATE
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})
    #return HttpResponse("crear_producto")

# DELETE
def borrar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'lista_productos.html', {'producto': producto})