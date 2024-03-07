from django.db import models

class Producto(models.Model):
    id = models.IntegerField(auto_created=True, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

