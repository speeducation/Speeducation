from django.shortcuts import render
from apps.alumnos.models import Alumno

# Create your views here.
def home(request):
    alumnos = Alumno.objects.all()
    context = {
        'alumnos' : alumnos,
    }

    return render(request,"maestros/alumnos_list.html", context)  #RENDERIZAMOS UN TEMPLATE, CON UN REQUEST ESPECIFICO Y UN CONTEXTO