from simple_rest_framework.services import BaseService
from .models import Maquina

class MaquinaService(BaseService):
    modelo = Maquina

    create_fields = []
    update_fields = []
    serialize_fields = ['nro_serie', 'tipo']
    foreign_fields = [
        {
            'campo': 'tipo',
            'serialize_fields': ['id', 'nombre', 'fabricante'],
            'foreign_fields': [
                {
                    'campo': 'fabricante',
                    'serialize_fields': ['id', 'nombre']
                }
            ]
        }
    ]

    unique_fields = []
    filter_fields = []
    sort_fields = []
