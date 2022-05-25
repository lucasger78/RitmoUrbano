from django.shortcuts import render
from django.http import HttpResponse
from AppRitmoUrbano.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre="Guitarra", profesor = "Lito Motoneta", horario= "16", dias="Martes, Jueves y Viernes", observaciones="Clase llena")
    
    curso.save
    
    documento = f"Datos del curso: {curso.nombre},\n el profe es: {curso.profesor},\n a las:{curso.horario} hs,\n Los {curso.dias},\n Pero {curso.observaciones}"
    
    return HttpResponse(documento)