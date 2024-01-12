from django.urls import path
from AppPizzas.views import *
urlpatterns = [
    path('',inicio, name="Inicio"),
    path('crearnuevaPizza/',agregarPizza, name="Crear Pizza"),
    path('Pizzas/',verPizza,name="Pizzas"),
    path('creador/',agregar_creador,name="Creadores"),
    path('asesor/',agregar_asesor,name="Asesores"),
    path('buscarPizza/', busquedaPizza, name="BuscarPizza"),
    path('resultados/',resultados,name="ResultadosBusqueda")
]