from django.db import models
from personas.models import Persona
from maquinas.models import Maquina

class ObraSocial(models.Model):
    nombre = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre
      
class Paciente(models.Model):
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def _str_(self):
        return self.persona
      
class HistoriaClinica(models.Model):
    fecha_hora = models.DateTimeField()
    descripcion = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def _str_(self):
        return self.paciente


class Turno(models.Model):
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    estado = models.CharField(max_length=50)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    persona_responsable = models.ForeignKey(Persona, on_delete=models.CASCADE)
    dialisis = models.ForeignKey('Dialisis', on_delete=models.CASCADE)

    def _str_(self):
       return f'Turno {self.estado} - {self.fecha_hora_inicio.strftime("%Y-%m-%d %H:%M")} - Paciente: {self.paciente}'

class Dialisis(models.Model):
    fecha_hora = models.DateTimeField()
    peso_in = models.FloatField()
    peso_out = models.FloatField()
    frecuencia_cardiaca = models.IntegerField()
    presion_a_in = models.IntegerField()
    presion_a_out = models.IntegerField()
    heparina_dosis = models.IntegerField()
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)

    def _str_(self):
        return f'Dialisis {self.id}'