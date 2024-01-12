from django import forms

# Create your models here.
class PizzaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=30)
    masa = forms.CharField(max_length=30)
    ingrediente1 = forms.CharField(max_length=30)
    ingrediente2 = forms.CharField(max_length=30)
    ingrediente3 = forms.CharField(max_length=30)
    ingrediente4 = forms.CharField(max_length=30)

class CreadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad =  forms.IntegerField()
    correo = forms.EmailField()

class AsesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    cod_ases =  forms.IntegerField()
    correo = forms.EmailField()
