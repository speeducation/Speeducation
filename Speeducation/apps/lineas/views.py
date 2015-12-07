from .models import Linea, Actividad, Conducta
from django.shortcuts import render, get_object_or_404
from .forms import AgregarLinea, AgregarActividad
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def lista_lineas(request):
    lineas = Linea.objects.all()
    lineas = lineas[::-1]
    return render(request, 'lineas/lista_lineas.html', {'lineas': lineas})

@login_required(login_url='/')
def editar_linea(request, pk):
    linea = get_object_or_404(Linea, pk=pk)
    if request.method == "POST":
        form = AgregarLinea(request.POST, instance = linea)
        if form.is_valid():
            linea = form.save(commit = False)
            linea.save()
            return redirect('/lineas/lista')
        else:
            return redirect('/')
    else:
        form = AgregarLinea(instance = linea)
    return render(request, 'lineas/editar_linea.html', {'form': form})

@login_required(login_url='/')
def agregar_linea(request):
    if request.method == "POST":
        form = AgregarLinea(request.POST)
        if form.is_valid():
            linea = form.save(commit=False)
            linea.save()
            return redirect('/lineas/lista')
    else:
        form = AgregarLinea()
    return render(request, 'lineas/editar_linea.html', {'form': form})

@login_required(login_url='/')
def eliminar_linea(request, pk):
    linea = Linea.objects.get(pk=pk)
    linea.delete()
    return redirect('/lineas/lista')

@login_required(login_url='/')
def detalles_linea(request, pk):
    url = get_base_url(request)
    linea = get_object_or_404(Linea, pk=pk)
    actividades = Actividad.objects.filter(linea=linea)

    context = {
        "linea" : linea,
        "actividades" : actividades,
        "url": url,
    }
    return render(request, 'lineas/detalles_linea.html', context)

@login_required(login_url='/')
def editar_actividad(request, pk):
    actividad = get_object_or_404(Actividad, pk=pk)
    if request.method == "POST":
        form = AgregarActividad(request.POST, instance = actividad)
        if form.is_valid():
            actividad = form.save(commit = False)
            actividad.save()
            return redirect(get_base_url(request).split('/actividad')[0])
        else:
            return redirect('/')
    else:
        form = AgregarActividad(instance = actividad)
    return render(request, 'lineas/editar_actividad.html', {'form': form})

@login_required(login_url='/')
def agregar_actividad(request, pk):
    url = get_base_url(request)
    linea = Linea.objects.get(pk=pk)
    if request.method == "POST":
        form = AgregarActividad(request.POST)
        if form.is_valid():
            actividad = form.save(commit=False)
            actividad.linea = linea
            actividad.save()
            return redirect(get_base_url(request).split('/actividad')[0])
    else:
        form = AgregarActividad()
    return render(request, 'lineas/editar_actividad.html', {'form': form})

@login_required(login_url='/')
def eliminar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    actividad.delete()
    return redirect(get_base_url(request).split('/actividad')[0])

def get_base_url(request):
    url = str(request)
    url = url.split("'", 1)
    url = url[1].replace("'>","")
    return url