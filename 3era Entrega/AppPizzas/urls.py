from django.urls import path
from AppPizzas.views import *
urlpatterns = [
    path('',inicio, name="Inicio"),
    path('crearnuevaPizza/',agregarPizza, name="Crear Pizza"),
    
    path('creador/',agregar_creador,name="Creadores"),
    path('asesor/',agregar_asesor,name="Asesores"),
    path('Pizzas/', busquedaPizza, name="Pizzas"),
    path('resultados/', resultados,name='resultadosBusq')
    
]

"""path('Pizzas/',verPizza,name="Pizzas"),

"""