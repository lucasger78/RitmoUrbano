from django.contrib import admin
from django.urls import path
from AppRitmoUrbano.models import Profesor, Curso, Alumno
from AppRitmoUrbano import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('clases', views.curso, name="Clases"),
    #path('alumno', views.alumno, name="Alumno"),
    #path('profesor', views.profesor, name="Profesor"),
    path('nosotros', views.nosotros, name='Nosotros'),
    
    path('contactoFormulario', views.contactoFormulario, name='ContactoFormulario'),
    path('cursoFormulario', views.cursoFormulario, name='CursoFormulario'), 
    path('curso',views.leerCurso, name="LeerCurso"),
    path('alumnoFormulario', views.alumnoFormulario, name='AlumnoFormulario'), 
    path('alumno',views.leerAlumno, name="LeerAlumno"),
    path('profesorFormulario', views.profesorFormulario, name='ProfesorFormulario'), 
    path('profesor',views.leerProfesor, name="LeerProfesor"),
    # path('eliminarPost/<post_titulo>/',views.eliminarPost, name="EliminarPost"),
    # path('editarPost/<post_titulo>/', views.editarPost, name="EditarPost"),
    
    #path('buscar',views.buscar,name="buscar"),
    path('resultadoBusqueda',views.busquedaCursos,name="busqueda"),
    path('resultadoBusqueda1',views.busquedaAlumnos,name="busqueda"),
    path('resultadoBusqueda2',views.busquedaProfesores,name="busqueda"),
    path('resultadoBusqueda3',views.busquedaClases,name="busqueda"),
]