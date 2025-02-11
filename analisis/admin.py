from django.contrib import admin
from .models import  Analisis, Categorias, Parametro, ResultadoAnalisis



@admin.register(Analisis)
class AnalisisAdmin(admin.ModelAdmin):
    list_display = ('fecha_hora', 'paciente')
    list_filter = ('fecha_hora',)  # Filtro por fecha
    search_fields = ('paciente__persona__nombre',)  # Búsqueda por nombre de paciente

@admin.register(Categorias)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)  # Búsqueda por nombre de categoría

@admin.register(Parametro)
class ParametroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria',)  # Filtro por categoría
    search_fields = ('nombre',)  # Búsqueda por nombre de parámetro

@admin.register(ResultadoAnalisis)
class ResultadoAnalisisAdmin(admin.ModelAdmin):
    list_display = ('analisis', 'parametro', 'valor')
    list_filter = ('analisis', 'parametro')  # Filtro por análisis y parámetro
    search_fields = ('analisis__paciente__persona__nombre', 'parametro__nombre')  # Búsqueda por paciente y parámetro

# categoria se cambio por categorias orque ya existia un categoria 