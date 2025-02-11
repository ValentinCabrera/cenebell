from django.db import models
from salud.models import Paciente

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    # funcion hepatica

class Parametro(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nombre} - {self.categoria}'
    # GOT
class Analisis(models.Model):
    fecha_hora = models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f'Análisis {self.paciente} - {self.fecha_hora.strftime("%Y-%m-%d %H:%M")}'

    # Analisis de Juan Perez 14 de noviemnbre
class ResultadoAnalisis(models.Model):
    parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    analisis = models.ForeignKey(Analisis, on_delete=models.CASCADE)

    def __str__(self):
        return f'Resultado {self.analisis} - {self.parametro} - Valor: {self.valor}'


# preguntar como hacer lo de los porcentahjes