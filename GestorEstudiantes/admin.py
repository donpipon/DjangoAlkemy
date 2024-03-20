from django.contrib import admin
from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "fecha_nacimiento", "edad", "calificacion" ] 
    search_fields = ["nombre", "apellido", "edad", "nota"]
    
    @admin.display(empty_value="-sin asignar-")
    def calificacion(self, obj):
        return obj.nota
    


admin.site.register(Estudiante, EstudianteAdmin)
