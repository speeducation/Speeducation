from django.shortcuts import render
from apps.alumnos.models import Alumno
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import AgregarMaestro
from django.shortcuts import redirect
from .models import Maestro
# Create your views here.
def home(request):
    alumnos = Alumno.objects.all()
    context = {
        'alumnos' : alumnos,
    }

    return render(request,"maestros/alumnos_list.html", context)  #RENDERIZAMOS UN TEMPLATE, CON UN REQUEST ESPECIFICO Y UN CONTEXTO

def lista_maestros(request):
    maestros = Maestro.objects.all()
    maestros = maestros[::-1]
    return render(request, 'maestros/lista_maestros.html', {'maestros': maestros})
