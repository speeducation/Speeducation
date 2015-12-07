from django.contrib import admin
from .models import Alumno, Periodo, PlanEstudio, Evaluacion

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Periodo)
admin.site.register(PlanEstudio)
admin.site.register(Evaluacion)
