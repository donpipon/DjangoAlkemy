from django.http import HttpResponse
from .requestRae import palabraAleatoria

def saludoBase(request):
    return HttpResponse("Hola Mundo")

def saludo(request, username):
    return HttpResponse("Hola, " + username + "!!!")

def despedida(request):
    return HttpResponse("Chau")

def buscarPalabra(request):
    palabra, definicion = palabraAleatoria()
    return HttpResponse(palabra)