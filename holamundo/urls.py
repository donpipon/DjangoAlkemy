
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludoBase, name="saludoBase"),
    path('saludo/<str:username>', views.saludo, name="saludo"),
    path('despedida/', views.despedida, name="despedida")
    ]