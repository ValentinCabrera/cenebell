from django.shortcuts import render
from simple_rest_framework.views import BaseSearchView

from .services import MaquinaService

class MaquinaSearchView(BaseSearchView, MaquinaService):
    pass 

