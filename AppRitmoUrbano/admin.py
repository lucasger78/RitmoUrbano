from pyexpat import model
from django.contrib import admin
#from jmespath import search
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class AlumnoResource(resources.ModelResource):
     class Meta:
          model = Alumno
          
class ProfesorResource(resources.ModelResource):
     class Meta:
          model = Profesor
          
class CursoResource(resources.ModelResource):
     class Meta:
          model = Curso
          
class ContactoResource(resources.ModelResource):
     class Meta:
          model = Contacto


class Alumnoadmin(ImportExportModelAdmin, admin.ModelAdmin):
     search_fields = ["nombre", "apellido", "curso"]
     list_display = ["nombre", "apellido", "curso"]
     list_editable = ["curso"]
     list_per_page = 20
     resourse_class = AlumnoResource

class Profesoradmin(ImportExportModelAdmin, admin.ModelAdmin):
     search_fields = ["nombre", "apellido", "curso"]
     list_display = ["nombre", "apellido", "curso"]
     list_editable = ["curso"]
     list_per_page = 20
     resourse_class = ProfesorResource

class Cursoadmin(ImportExportModelAdmin, admin.ModelAdmin):
     list_display = ["clase", "profesor"]
     list_editable = ["profesor"]
     search_fields = ["clase", "profesor"]
     list_per_page = 5
     resourse_class = CursoResource
     
class Contactoadmin(ImportExportModelAdmin, admin.ModelAdmin):
     list_display = ["nombre", "email", "telefono"]
     search_fields = ["nombre", "email", "telefono"]
     list_per_page = 10
     resourse_class = ContactoResource
     
admin.site.register(Alumno, Alumnoadmin)

admin.site.register(Profesor, Profesoradmin)

admin.site.register(Curso, Cursoadmin)

admin.site.register(Contacto, Contactoadmin)


