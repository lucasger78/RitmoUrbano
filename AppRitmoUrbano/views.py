import email
from email.mime import image
#from tkinter import _ImageSpec, image_types
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
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    
    return render(request, 'AppRitmoUrbano/inicio.html')

def curso(request):
    
    return render(request, 'AppRitmoUrbano/clases.html')

def alumno(request):
    
    return render(request, 'AppRitmoUrbano/alumno.html')   

def profesor(request):
    
    return render(request, 'AppRitmoUrbano/profesor.html')

def nosotros(request):
    
    return render(request, "AppRitmoUrbano/nosotros.html")

# def contacto(request):
#     data = {'form': ContactoFormulario}
    
#     if request.method == 'POST':
#         formulario = ContactoFormulario(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             data["mensaje"] = "Mensaje Enviado"
#         else:
#             data['form'] = formulario
        
    
#     return render(request, "AppRitmoUrbano/contacto.html", data)


#------1 - CREATE -------
def cursoFormulario(request):
    
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST, request.FILES)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
         
            informacion = miFormulario.cleaned_data
            

            # tituloNuevo = informacion['titulo']
            # tituloChecker = Post.objects.filter(titulo__contains = tituloNuevo)
            # if tituloChecker.exists():
            #      return render(request, "AppLuckApp/postFormulario.html", {"mensaje":"Ya hay un post con el mismo título !","miFormularioBlog":miFormulario})
            # else:
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
            

            # tituloNuevo = informacion['titulo']
            # tituloChecker = Post.objects.filter(titulo__contains = tituloNuevo)
            # if tituloChecker.exists():
            #      return render(request, "AppLuckApp/postFormulario.html", {"mensaje":"Ya hay un post con el mismo título !","miFormularioBlog":miFormulario})
            # else:
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
    # try:
    #     avatar = Avatar.objects.get(user=request.user)
    # except:
    #     avatar = None

    curso = Curso.objects.all()
    
    contexto= {"curso":curso} 
    
    return render(request, "AppRitmoUrbano/leercurso.html", contexto)

def leerAlumno(request):
    # try:
    #     avatar = Avatar.objects.get(user=request.user)
    # except:
    #     avatar = None

    alumno = Alumno.objects.all()
    
    contexto= {"alumno":alumno} 
    
    return render(request, "AppRitmoUrbano/leeralumno.html", contexto)

def leerProfesor(request):
    # try:
    #     avatar = Avatar.objects.get(user=request.user)
    # except:
    #     avatar = None

    profesor = Profesor.objects.all()
    
    contexto= {"profesor":profesor} 
    
    return render(request, "AppRitmoUrbano/leerprofesor.html", contexto)


# #------3 - UPDATE -------   

# def editarPost(request, post_titulo):
#     try:
#         avatar = Avatar.objects.get(user=request.user)
#     except:
#         avatar = None

#     post = Post.objects.get(titulo=post_titulo)
    
#     if request.method == "POST":

#         miFormulario = PostFormulario(request.POST, request.FILES)                                                                     

#         print(miFormulario)
        
#         if miFormulario.is_valid:
            
#             informacion = miFormulario.cleaned_data

#             #tituloNuevo = informacion['titulo']
#             #Para que se pueda editar el post sin tener que editar el título
#             #tituloChecker = Post.objects.filter(titulo__contains = tituloNuevo)

#             #if tituloChecker.exists():
#                 #return render(request, "AppLuckApp/editarPost.html", {"mensaje":"Ya hay un post con el mismo título ! Si no quieres editar, vuelve a la página de blogs","miFormularioEditPost":miFormulario})
#             #else:

#             post.titulo = informacion['titulo']
#             post.subtitulo = informacion['subtitulo']
#             post.contenido = informacion['contenido']
#             post.fecha = informacion['fecha']

#             try:
#                 post.imagen = informacion['imagen']
#             except KeyError:
#                 post.imagen = post.imagen


#             post.save()                                                                               
#             return render(request, "AppLuckApp/editarPost.html", {"mensaje":"Post modificado!","miFormularioEditPost":miFormulario, "avatar":avatar})                                                                     
#     else:  
        
#         miFormulario = PostFormulario(initial={'titulo':post.titulo, 'subtitulo':post.subtitulo, 'contenido':post.contenido, 'fecha':post.fecha,'imagen':post.imagen, "avatar":avatar})
        
#     return render(request, "AppLuckApp/editarPost.html", {"miFormularioEditPost":miFormulario, "post":post, "avatar":avatar})



# #------4 - DELETE -------  
# def eliminarPost(request, post_titulo):
#     try:
#         avatar = Avatar.objects.get(user=request.user)
#     except:
#         avatar = None
    
#     post = Post.objects.get(titulo=post_titulo)
#     post.delete()
    
#     #vuelvo al menú
#     post = Post.objects.all()
    
#     contexto= {"post":post, "avatar":avatar} 
    
#     return render(request, "AppLuckApp/leerPost.html", contexto)


# #-------------REGISTRAR------------

# # def register(request):
    
# #     if request.method == 'POST':
        
# #         #form = UserCreationForm(request.POST)
# #         form = UserRegisterForm(request.POST, request.FILES)
        
# #         if form.is_valid():
            
# #             username = form.cleaned_data['username']
# #             form.save()

# #             return render(request, "AppLuckApp/registro.html", {"mensaje":"Usuario Creado! Ya puedes inciar sesión"})
# #     else:
        
# #         form = UserRegisterForm()
        
# #     return render(request, "AppLuckApp/registro.html", {"registerForm":form})


# #-------------EDITAR USUARIO-------------

# @login_required
# def editarPerfil(request): 
#     try:
#         avatar = Avatar.objects.get(user=request.user)
#     except:
#         avatar = None

#     usuario = request.user

#     if request.method == 'POST':

#         myForm = UserEditForm(request.POST, request.FILES)

#         if myForm.is_valid():

#             informacion =  myForm.cleaned_data
            
#             usuario.email = informacion['email']
#             usuario.password1 = informacion['password1']
#             usuario.password2 = informacion['password2']

#             usuario.save()
            
#             return render(request, "AppLuckApp/index.html")  
#     else:
        
#          myForm = UserEditForm(initial={'email':usuario.email,'last_name':usuario.last_name,'first_name':usuario.first_name, "avatar":avatar})
    
#     return render(request, "AppLuckApp/editarPerfil.html", {"miFormularioEditPerfil": myForm, "usuario":usuario,"avatar":avatar})



# def buscar(request):
    
#     return render (request,'AppRitmoUrbano/buscarCurso.html')


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