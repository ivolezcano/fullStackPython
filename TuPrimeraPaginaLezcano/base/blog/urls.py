from django.urls import path
from .views import listar_entradas, agregar_entrada, buscar_entrada

urlpatterns = [
    path('', agregar_entrada, name='agregar_entrada'),
    path('listar/', listar_entradas, name='listar_entradas'),
    path('buscar/', buscar_entrada, name='buscar_entrada'),
]