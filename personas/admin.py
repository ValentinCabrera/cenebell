from django.contrib import admin
from .models import Rol, Persona

admin.site.register(Rol)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rol')