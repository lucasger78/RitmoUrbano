from django.db import models

# Create your models here.
class Alumno(models.Model):

    #Avatar(ver como se carga en models este item desde AppLuckApp)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    email = models.EmailField
    telefono = models.IntegerField()
    observaciones = models.CharField(max_length=1500)

class Profesor(models.Model):

    #Avatar(ver como se carga en models este item desde AppLuckApp)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    email = models.EmailField
    telefono = models.IntegerField()
    observaciones = models.CharField(max_length=1500)

class Curso(models.Model):

    #Avatar(ver como se carga en models este item desde AppLuckApp)
    nombre = models.CharField(max_length=40)
    profesor = models.CharField(max_length=40)
    dias = models.CharField(max_length=40)
    horario = models.IntegerField()
    observaciones = models.CharField(max_length=1500)