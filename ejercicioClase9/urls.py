from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_productos, name="lista_productos"),
    path('lista_productos/', views.lista_productos, name="lista_productos"),
    path('crear_producto', views.crear_producto, name="crear_producto"),
    path('task/<int:id>/borrar/', views.borrar, name='borrar'),

]