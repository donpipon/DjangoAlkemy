from django.http import HttpResponse


def saludo(request, username):
    return HttpResponse("Hola, " + username + "!!!")


def despedida(request):
    return HttpResponse("Chau")


from django.shortcuts import render

# Create your views here.
