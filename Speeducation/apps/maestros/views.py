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

def detalles_maestro(request, pk):
    maestro = get_object_or_404(Maestro, pk=pk)
    return render(request, 'maestros/detalles_maestro.html', {'maestro': maestro})

def editar_maestro(request, pk):
    maestro = get_object_or_404(Maestro, pk=pk)
    if request.method == "POST":
        form = AgregarMaestro(request.POST, instance = maestro)
        if form.is_valid():
            maestro = form.save(commit = False)
            maestro.save()
            return redirect('/maestro/'+str(maestro.pk), pk=maestro.pk)
        else:
            form = AgregarMaestro(instance = maestro)
            return redirect('/maestros/lista')
    else:
        form = AgregarMaestro(instance = maestro)
    return render(request, 'maestros/editar_maestro.html', {'form': form})

def agregar_maestro(request):
    if request.method == "POST":
        form = AgregarMaestro(request.POST)
        if form.is_valid():
            maestro = form.save(commit=False)
            maestro.save()
            return redirect('/maestro/'+str(maestro.pk), pk=maestro.pk)
    else:
        form = AgregarMaestro()
    return render(request, 'maestros/editar_maestro.html', {'form': form})

def eliminar_maestro(request, pk):
    maestro = Maestro.objects.get(pk=pk)
    maestro.delete()
    maestro = Maestro.objects.all()
    maestro = maestro[::-1]
    return render(request, 'maestros/lista_maestros.html', {'maestros': maestros})
