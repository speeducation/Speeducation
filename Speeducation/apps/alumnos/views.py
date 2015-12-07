from django.shortcuts import render
from django.utils import timezone
from .models import Alumno, PlanEstudio
from django.shortcuts import render, get_object_or_404
from .forms import AgregarAlumno, AgregarPlan
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
    url = get_base_url(request)
    alumno = get_object_or_404(Alumno, pk=pk)
    planes_estudio = PlanEstudio.objects.filter(alumno = alumno)
    context = {
        'alumno' : alumno,
        'planes_estudio' : planes_estudio,
        'url' : url,
    }
    return render(request, 'alumnos/detalles_alumno.html', context)

@login_required(login_url='/')
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AgregarAlumno(request.POST, instance = alumno)
        if form.is_valid():
            alumno = form.save(commit = False)
            alumno.save()
            return redirect('/alumnos/lista/')
        else:
            return redirect('/alumnos/lista/')
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

##############PLAN DE ESTUDIOS DE UN ALUMNO ESPECIFICO####################

@login_required(login_url='/')
def agregar_plan(request, pk):
    if request.method == "POST":
        alumno =  Alumno.objects.get(pk=pk)
        form = AgregarPlan(request.POST)
        planes = PlanEstudio.objects.filter(alumno = alumno)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.alumno = alumno
            if not check_duplicate_plan(planes, plan):
                plan.save()
            return redirect('/alumno/'+str(alumno.pk), pk=alumno.pk)
    else:
        form = AgregarPlan()
    return render(request, 'alumnos/editar_plan.html', {'form': form})

@login_required(login_url='/')
def editar_plan(request, pk):
    plan = get_object_or_404(PlanEstudio, pk=pk)
    print plan
    if request.method == "POST":
        form = AgregarPlan(request.POST, instance = plan)
        if form.is_valid():
            plan = form.save(commit = False)
            plan.save()
            return redirect(get_base_url(request).split('/plan')[0])
        else:
            return redirect('/')
    else:
        form = AgregarPlan(instance = plan)
    return render(request, 'alumnos/editar_plan.html', {'form': form})

@login_required(login_url='/')
def eliminar_plan(request, pk):
    plan = PlanEstudio.objects.get(pk=pk)
    plan.delete()
    return redirect(get_base_url(request).split('/plan')[0])

#############################COMPORTAMIENTO###########################

##############################FUNCIONES###############################

def check_duplicate_plan(planes, plan):
    for aux in planes:
        if aux.linea == plan.linea and aux.periodo == plan.periodo:
            return True
    return False

def get_base_url(request):
    url = str(request)
    url = url.split("'", 1)
    url = url[1].replace("'>","")
    return url