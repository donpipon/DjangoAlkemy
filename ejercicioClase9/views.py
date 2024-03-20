from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponse, JsonResponse
import json
from django.template import Template, Context

# READ

# Alternativa para cargar el template como respuetsa Http + contexto (util en apps mas grandes)  
# def lista_productos(request):
#     productos = Producto.objects.all()
    
#     ruta = "ejercicioClase9/templates/lista_productos.html"
#     doc = open(ruta)
#     plantilla = Template(doc.read())
#     doc.close()
    
#     contexto = Context({'productos': productos})

#     documento = plantilla.render(contexto)
#     return HttpResponse(documento)


def lista_productos(request):
     productos = Producto.objects.all()
     form = ProductoForm(request.POST)
     return render(request, 'lista_productos.html', {'form': form, 'productos': productos})


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
        productos = Producto.objects.all()
        return redirect('lista_productos')
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})