from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Estudiante

def listaEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def crearEstudiante(request, nombre, apellido, edad, nota):
    estudiante = Estudiante.objects.create(nombre=nombre, apellido=apellido, edad=edad, nota=nota)
    return render(request, 'crear_estudiante.html', {'estudiante': estudiante})

def modificarEstudiantes(request, id, nota):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.nota = nota
    estudiante.save()
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def borrarEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})



