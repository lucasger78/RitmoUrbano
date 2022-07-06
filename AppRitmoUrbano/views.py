import email
from email.mime import image
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppRitmoUrbano.models import Alumno, Profesor, models
from AppRitmoUrbano.forms import AlumnoFormulario, ProfesorFormulario, CursoFormulario, ContactoFormulario
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    return render(request, 'AppRitmoUrbano/index.html')

def curso(request):
    
    return render(request, 'AppRitmoUrbano/clases.html')

def modalidades(request):
    
    return render(request, 'AppRitmoUrbano/modalidades.html')

def staff(request):
    
    return render(request, 'AppRitmoUrbano/staff.html')

def alumno(request):
    
    return render(request, 'AppRitmoUrbano/alumno.html')   

def profesor(request):
    
    return render(request, 'AppRitmoUrbano/profesor.html')

def nosotros(request):
    
    return render(request, "AppRitmoUrbano/nosotros.html")



#------1 - CREATE -------
def cursoFormulario(request):
    
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST, request.FILES)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
         
            informacion = miFormulario.cleaned_data
        

            
            curso = Curso(clase=informacion['clase'], profesor=informacion['profesor'], dia=informacion['dia'],
                              horario=informacion['horario'], imagen=informacion['imagen'], observaciones=informacion['observaciones']) 
            curso.save()
                                                                                            
            return render(request, "AppRitmoUrbano/cursoFormulario.html", {"mensaje":"Curso creado!"})                                                                
    else:
        miFormulario = CursoFormulario()     
                                                                                                                            
    return render (request, "AppRitmoUrbano/cursoFormulario.html", {"miFormularioBlog":miFormulario})


def alumnoFormulario(request):
    
    if request.method == "POST":
        miFormulario = AlumnoFormulario(request.POST, request.FILES)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
         
            informacion = miFormulario.cleaned_data
            

           
            alumno = Alumno(nombre=informacion['nombre'], apellido=informacion['apellido'], curso=informacion['curso'],
                               telefono=informacion['telefono'], imagen=informacion['imagen'], observaciones=informacion['observaciones']) 
            alumno.save()
                                                                                            
            return render(request, "AppRitmoUrbano/alumnoFormulario.html", {"mensaje":"Alumno creado!"})                                                                
    else:
        miFormulario = AlumnoFormulario()     
                                                                                                                            
    return render (request, "AppRitmoUrbano/alumnoFormulario.html", {"miFormularioBlog":miFormulario})


def profesorFormulario(request):
    
   
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST, request.FILES)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
         
            informacion = miFormulario.cleaned_data           
            
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], curso=informacion['curso'],
                               telefono=informacion['telefono'], imagen=informacion['imagen'], observaciones=informacion['observaciones']) 
            profesor.save()
                                                                                            
            return render(request, "AppRitmoUrbano/profesorFormulario.html", {"mensaje":"Profesor creado!"})                                                                
    else:
        miFormulario = ProfesorFormulario()     
                                                                                                                            
    return render (request, "AppRitmoUrbano/profesorFormulario.html", {"miFormularioBlog":miFormulario})


def contactoFormulario(request):
     
    
    if request.method == "POST":
        miFormulario = ContactoFormulario(request.POST, request.FILES)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
         
            informacion = miFormulario.cleaned_data
            
            contacto = Contacto(nombre=informacion['nombre'], email=informacion['email'], telefono=informacion['telefono'], mensaje=informacion['mensaje']) 
                     
            contacto.save()
                                                                                            
            return render(request, "AppRitmoUrbano/contactoFormulario.html", {"mensaje":"Mensaje Enviado!"})                                                                
    else:
        miFormulario = ContactoFormulario()     
                                                                                                                            
    return render (request, "AppRitmoUrbano/contactoFormulario.html", {"miFormularioBlog":miFormulario})

#------2 - READ -------
def leerCurso(request):    

    curso = Curso.objects.all()
    
    contexto= {"curso":curso} 
    
    return render(request, "AppRitmoUrbano/leercurso.html", contexto)


def leerAlumno(request):
    
    alumno = Alumno.objects.all()
    
    contexto= {"alumno":alumno} 
    
    return render(request, "AppRitmoUrbano/leeralumno.html", contexto)


def leerProfesor(request):
    
    profesor = Profesor.objects.all()
    
    contexto= {"profesor":profesor} 
    
    return render(request, "AppRitmoUrbano/leerprofesor.html", contexto)




    return render (request,'AppRitmoUrbano/buscarCurso.html')


#BUSQUEDA CURSOS
def busquedaCursos(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        listacurso = Curso.objects.filter(clase__contains = query)

        return render(request, 'AppRitmoUrbano/resultadoBusqueda.html',{'query':query,'curso':listacurso})
   
    
#BUSQUEDA ALUMNOS
def busquedaAlumnos(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        listaalumno = Alumno.objects.filter(nombre__contains = query)

        return render(request, 'AppRitmoUrbano/resultadoBusqueda1.html',{'query':query,'alumno':listaalumno})
    
#BUSQUEDA PROFESOR
def busquedaProfesores(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        listaprofesor = Profesor.objects.filter(nombre__contains = query)

        return render(request, 'AppRitmoUrbano/resultadoBusqueda2.html',{'query':query,'profesor':listaprofesor})
    
#BUSQUEDA CLASES

def busquedaClases(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        listaclase = Curso.objects.filter(nombre__contains = query)

        return render(request, 'AppRitmoUrbano/resultadoBusqueda3.html',{'query':query,'clase':listaclase})