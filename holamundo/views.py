from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola Mundo")


def despedida(request):
    return HttpResponse("Chau")


from django.shortcuts import render

# Create your views here.
