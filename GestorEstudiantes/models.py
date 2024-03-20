from django.db import models

class Estudiante(models.Model):
    id = models.IntegerField(auto_created=True, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    edad = models.IntegerField(max_length=3)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nota = models.IntegerField(max_length=2, null=True, blank=True)

    def __str__(self):
        return self.nombre

