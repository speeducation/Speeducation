from .models import Linea, Actividad, Conducta
from django.shortcuts import render, get_object_or_404
from .forms import AgregarLinea, AgregarActividad, AgregarConducta
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def lista_lineas(request):
    lineas = Linea.objects.all()
    lineas = lineas[::-1]
    return render(request, 'lineas/lista_lineas.html', {'lineas': lineas})

############################LINEA#################################

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def eliminar_linea(request, pk):
    linea = Linea.objects.get(pk=pk)
    linea.delete()
    return redirect('/lineas/lista')

@login_required(login_url='/login/')
def detalles_linea(request, pk):
    url = get_base_url(request)
    linea = get_object_or_404(Linea, pk=pk)
    actividades = Actividad.objects.filter(linea=linea)
    conductas =  Conducta.objects.filter(linea=linea)

    context = {
        "linea" : linea,
        "actividades" : actividades,
        "conductas" : conductas,
        "url": url,
    }
    return render(request, 'lineas/detalles_linea.html', context)

####################ACTIVIDADES#################################

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def agregar_actividad(request, pk):
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

@login_required(login_url='/login/')
def eliminar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    actividad.delete()
    return redirect(get_base_url(request).split('/actividad')[0])

##############################CONDUCTAS###########################

@login_required(login_url='/login/')
def editar_conducta(request, pk):
    conducta = get_object_or_404(Conducta, pk=pk)
    if request.method == "POST":
        form = AgregarConducta(request.POST, instance = conducta)
        if form.is_valid():
            conducta = form.save(commit = False)
            conducta.save()
            return redirect(get_base_url(request).split('/conducta')[0])
        else:
            return redirect('/')
    else:
        form = AgregarConducta(instance = conducta)
    return render(request, 'lineas/editar_conducta.html', {'form': form})

@login_required(login_url='/login/')
def agregar_conducta(request, pk):
    linea = Linea.objects.get(pk=pk)
    if request.method == "POST":
        form = AgregarConducta(request.POST)
        if form.is_valid():
            conducta = form.save(commit=False)
            conducta.linea = linea
            conducta.save()
            return redirect(get_base_url(request).split('/conducta')[0])
    else:
        form = AgregarConducta()
    return render(request, 'lineas/editar_conducta.html', {'form': form})

@login_required(login_url='/login/')
def eliminar_conducta(request, pk):
    conducta = Conducta.objects.get(pk=pk)
    conducta.delete()
    return redirect(get_base_url(request).split('/conducta')[0])


###############################FUNCIONES#############################

def get_base_url(request):
    url = str(request)
    url = url.split("'", 1)
    url = url[1].replace("'>","")
    return url
