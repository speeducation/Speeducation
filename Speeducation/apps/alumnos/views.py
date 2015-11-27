from django.shortcuts import render
from django.utils import timezone
from .models import Alumno
from django.shortcuts import render, get_object_or_404
from .forms import AgregarAlumno
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    alumnos = Alumno.objects.all()
    return render(request, 'base/login.html', {'alumnos': alumnos})

@login_required(login_url='/')
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    alumnos = alumnos[::-1]
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': alumnos})

@login_required(login_url='/')
def detalles_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumnos/detalles_alumno.html', {'alumno': alumno})

@login_required(login_url='/')
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AgregarAlumno(request.POST, instance = alumno)
        if form.is_valid():
            alumno = form.save(commit = False)
            alumno.save()
            return redirect('/alumno/'+str(alumno.pk), pk=alumno.pk)
        else:
            form = AgregarAlumno(instance = alumno)
            return redirect('/')
    else:
        form = AgregarAlumno(instance = alumno)
    return render(request, 'alumnos/editar_alumno.html', {'form': form})

@login_required(login_url='/')
def agregar_alumno(request):
    if request.method == "POST":
        form = AgregarAlumno(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
            return redirect('/alumno/'+str(alumno.pk), pk=alumno.pk)
    else:
        form = AgregarAlumno()
    return render(request, 'alumnos/editar_alumno.html', {'form': form})

@login_required(login_url='/')
def eliminar_alumno(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    alumno.delete()
    alumnos = Alumno.objects.all()
    alumnos = alumnos[::-1]
    return render(request, 'alumnos/lista_alumnos.html', {'alumnos': alumnos})
