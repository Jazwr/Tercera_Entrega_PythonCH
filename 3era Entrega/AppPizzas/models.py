from django.db import models

# Create your models here.
class Pizza(models.Model):
    nombre = models.CharField(max_length=30)
    tamaño = models.CharField(max_length=30)
    masa = models.CharField(max_length=30)
    ingrediente1 = models.CharField(max_length=30)
    ingrediente2 = models.CharField(max_length=30)
    ingrediente3 = models.CharField(max_length=30)
    ingrediente4 = models.CharField(max_length=30)

class Creador(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    correo = models.EmailField()

class Asesor(models.Model):
    nombre = models.CharField(max_length=30)
    cod_ases = models.IntegerField()
    correo = models.EmailField()


