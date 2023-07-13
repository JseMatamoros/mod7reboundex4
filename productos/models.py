from django.db import models
from django.urls import reverse
# Create your models here.
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("detalle_producto", args=[self.id])