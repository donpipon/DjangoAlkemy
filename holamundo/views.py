from django.http import HttpResponse

def saludoBase(request):
    return HttpResponse("Hola Mundo")

def saludo(request, username):
    return HttpResponse("Hola, " + username + "!!!")

def despedida(request):
    return HttpResponse("Chau")

