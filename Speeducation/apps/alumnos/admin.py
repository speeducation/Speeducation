from django.contrib import admin
from .models import Alumno, Periodo, Evaluacion, Comportamiento

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Periodo)
admin.site.register(Evaluacion)
admin.site.register(Comportamiento)
