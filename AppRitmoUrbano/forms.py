from dataclasses import field, fields
import email
from django import forms



from .models import *

class CursoFormulario(forms.Form):
    clase = forms.CharField()
    profesor = forms.CharField()
    dia = forms.CharField() 
    horario = forms.TimeField()
    observaciones = forms.CharField()
    imagen = forms.ImageField()

    class Meta:
        model = ConnectionResetError
        fields = ['nombre', 'profesor', 'dia', 'horario', 'observaciones', 'imagen']
        help_texts = {k:"" for k in fields}
        
        
class AlumnoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    curso = forms.CharField() 
    email = forms.EmailField()
    telefono = forms.IntegerField()
    observaciones = forms.CharField()
    imagen = forms.ImageField()

    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'curso', 'email', 'telefono', 'observaciones', 'imagen']
        help_texts = {k:"" for k in fields}
        
        
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    curso = forms.CharField() 
    email = forms.EmailField()
    telefono = forms.IntegerField()
    observaciones = forms.CharField()
    imagen = forms.ImageField()

    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'curso', 'email', 'telefono', 'observaciones', 'imagen']
        help_texts = {k:"" for k in fields}
        
class ContactoFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    mensaje = forms.CharField()
    

    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'mensaje']
        help_texts = {k:"" for k in fields}
    


