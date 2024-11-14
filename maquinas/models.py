from django.db import models
from personas.models import Persona

class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Maquina(models.Model):
    nro_serial = models.CharField(max_length=50)
    horas_uso = models.IntegerField()
    disponible = models.BooleanField()

    def __str__(self):
        return self.nro_serial

class VisitaMantenimiento(models.Model):
    fecha_hora = models.DateTimeField()
    tecnico = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha_hora) + ' - ' + self.tecnico.__str__()

class Mantenimiento(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)
    visita = models.ForeignKey(VisitaMantenimiento, on_delete=models.CASCADE)
    horas_trabajo = models.IntegerField()
    observaciones = models.TextField()
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return self.maquina.__str__() + ' - ' + self.tipo.__str__() + ' - ' + self.visita.__str__() + ' - ' + str(self.fecha_hora)