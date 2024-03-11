
from django.urls import path
from . import views

urlpatterns = [

    path('', views.listaEstudiantes, name="estudiantes"),
    path('modificar/<int:id>/<int:nota>', views.modificarEstudiantes, name="modificar"),
    path('crear/<str:nombre>/<str:apellido>/<int:edad>/<int:nota>', views.crearEstudiante, name="crear"),
    path('borrar/<int:id>', views.borrarEstudiante, name='borrar'),

]