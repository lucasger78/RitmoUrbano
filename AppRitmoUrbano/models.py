from distutils.log import info
import email
from re import M
from django.db import models

# Create your models here.
class Alumno(models.Model):
    
    
    imagen = models.ImageField(upload_to='media/alumnos', null=True, blank = True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    email = models.EmailField
    telefono = models.IntegerField()
    observaciones = models.TextField()
    
    def __str__(self):
        return '%s %s %s'%(self.apellido, self.nombre, self.curso)

class Profesor(models.Model):
    
    
    imagen = models.ImageField(upload_to='media\media\profesores', null=True, blank = True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    email = models.EmailField
    telefono = models.IntegerField()
    observaciones = models.TextField()
    
    def __str__(self):
        return '%s %s %s'%(self.apellido, self.nombre, self.curso)

class Curso(models.Model):

    
    imagen = models.ImageField(upload_to='media/cursos', null=True, blank = True)
    clase = models.CharField(max_length=40)
    profesor = models.CharField(max_length=40)
    dia = models.CharField(max_length=40)
    horario = models.TimeField()
    observaciones = models.TextField()
    
    def __str__(self):
        return "%s %s"%(self.clase, self.profesor)
    
    
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField(null=True)
    telefono = models.IntegerField()
    mensaje = models.TextField()
    
    def __str__(self):
        return "%s %s %s"%(self.nombre, self.email, self.telefono)
        
     