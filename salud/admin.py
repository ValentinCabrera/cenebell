from django.contrib import admin
from .models import ObraSocial, Paciente, HistoriaClinica, Turno, Dialisis

@admin.register(ObraSocial)
class ObraSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('obra_social', 'persona')

@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('paciente','fecha_hora')

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('estado', 'fecha_hora_inicio', 'fecha_hora_fin', 'paciente', 'persona_responsable') 

@admin.register(Dialisis)
class DialisisAdmin(admin.ModelAdmin):
    list_display = ('fecha_hora', 'peso_in', 'peso_out', 'frecuencia_cardiaca', 'presion_a_in', 'presion_a_out', 'heparina_dosis', 'maquina')