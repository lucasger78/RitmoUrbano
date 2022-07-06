from django.contrib import admin
from django.urls import path
from AppRitmoUrbano.models import Profesor, Curso, Alumno
from AppRitmoUrbano import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('clases', views.curso, name="Clases"),
    path('modalidades', views.modalidades, name="Modalidades"),
    path('staff', views.staff, name="Staff"),   
    path('nosotros', views.nosotros, name='Nosotros'),
    
    path('contactoFormulario', views.contactoFormulario, name='ContactoFormulario'),
    path('cursoFormulario', views.cursoFormulario, name='CursoFormulario'), 
    path('curso',views.leerCurso, name="LeerCurso"),
    path('alumnoFormulario', views.alumnoFormulario, name='AlumnoFormulario'), 
    path('alumno',views.leerAlumno, name="LeerAlumno"),
    path('profesorFormulario', views.profesorFormulario, name='ProfesorFormulario'), 
    path('profesor',views.leerProfesor, name="LeerProfesor"),
  
    path('resultadoBusqueda',views.busquedaCursos,name="busqueda"),
    path('resultadoBusqueda1',views.busquedaAlumnos,name="busqueda"),
    path('resultadoBusqueda2',views.busquedaProfesores,name="busqueda"),
    path('resultadoBusqueda3',views.busquedaClases,name="busqueda"),
]