from django.contrib import admin

from .models import Mantenimiento, Maquina, TipoMantenimiento, VisitaMantenimiento

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('maquina', 'tipo', 'visita', 'horas_trabajo', 'fecha_hora')

@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ('nro_serial', 'horas_uso', 'disponible')

@admin.register(TipoMantenimiento)
class TipoMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(VisitaMantenimiento)
class VisitaMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha_hora', 'tecnico')

