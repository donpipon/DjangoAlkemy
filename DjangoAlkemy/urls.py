
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('holamundo.urls')),
    path('', include('ejercicioClase9.urls')),
    path('', include('GestorEstudiantes.urls')),
]
