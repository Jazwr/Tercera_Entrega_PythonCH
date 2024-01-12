from django.http import HttpResponse
from django.shortcuts import render
from AppPizzas.models import *
from AppPizzas.forms import *
# Create your views here.

def inicio(request):
    return render(request,"AppPizzas/inicio.html")


def agregarPizza(request):

    if request.method=="POST":
        info_formulario = PizzaFormulario(request.POST)
        
        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nueva_pizza = Pizza(nombre=info["nombre"],tamaño=info["tamaño"],masa=info["masa"],ingrediente1=info["ingrediente1"],ingrediente2=info["ingrediente2"],ingrediente3=info["ingrediente3"],ingrediente4=info["ingrediente4"])
            #,ingrediente5=info["ingrediente5"],ingrediente6=info["ingrediente6"])
            nueva_pizza.save()
            return render (request,"AppPizzas/todas_pizzas.html")
            #print(info)
        #print(info_formulario)

    else:
        nuevoformulario = PizzaFormulario()
    return render(request,"AppPizzas/crear_pizza.html",{"nuevo":nuevoformulario})

def verPizza(request):

    return render(request,"AppPizzas/todas_pizzas.html")

def agregar_asesor(request):
    if request.method=="POST":
        asesor_formulario = AsesorFormulario(request.POST)
        
        if asesor_formulario.is_valid():
            ases = asesor_formulario.cleaned_data
            datos_asesor = Asesor(nombre=ases["nombre"],cod_ases=ases["cod_ases"],ases=ases["correo"])
            #,ingrediente5=info["ingrediente5"],ingrediente6=info["ingrediente6"])
            datos_asesor.save()
            return render (request,"AppPizzas/asesor.html")
            #print(info)
        #print(info_formulario)

    else:
        nuevoasesor = AsesorFormulario()
    return render(request,"AppPizzas/asesor.html",{"nuevo_asesor":nuevoasesor})


def agregar_creador(request):
    if request.method=="POST":
        creador_formulario = CreadorFormulario(request.POST)
        
        if creador_formulario.is_valid():
            cread = creador_formulario.cleaned_data
            datos_creador = Creador(nombre=cread["nombre"],edad=cread["edad"],correo=cread["correo"])
            #,ingrediente5=info["ingrediente5"],ingrediente6=info["ingrediente6"])
            datos_creador.save()
            return render (request,"AppPizzas/inicio.html")
        
    else:
        nuevocreador = CreadorFormulario()
    return render(request,"AppPizzas/creador.html",{"nuevo_creador":nuevocreador})



def busquedaPizza(request):
    
    return render(request,"AppPizzas/inicio.html")

def resultados(request):
    if request.GET["BusquedaPizza"]:

        BuscarPizza=request.GET["BusquedaPizza"]
        Nombres=Pizza.objects.filter(BuscarPizza__icontains=BuscarPizza)
    
        return render(request,"AppPizzas/inicio.html", {"tamaño":BuscarPizza,"Nombre_Pizza":Nombres})
    
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

