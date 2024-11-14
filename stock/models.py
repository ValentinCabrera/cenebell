from django.db import models
from maquinas.models import Mantenimiento

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Material(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock_minimo = models.IntegerField()
    stock_actual = models.IntegerField()

    def __str__(self):
        return self.nombre