from django.shortcuts import render
from apps.alumnos.models import Alumno
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import AgregarMaestro
from .forms import AgregarUsuario
from django.shortcuts import render_to_response,redirect
from .models import Maestro
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    alumnos = Alumno.objects.all()
    context = {
        'alumnos' : alumnos,
    }

    return render(request,"maestros/alumnos_list.html", context)  #RENDERIZAMOS UN TEMPLATE, CON UN REQUEST ESPECIFICO Y UN CONTEXTO


def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/alumnos/lista')
    return render_to_response('base/login.html', context_instance=RequestContext(request))

@login_required(login_url='/')
def lista_maestros(request):
    maestros = Maestro.objects.all()
    maestros = maestros[::-1]
    return render(request, 'maestros/lista_maestros.html', {'maestros': maestros})

@login_required(login_url='/')
def detalles_maestro(request, pk):
    maestro = get_object_or_404(Maestro, pk=pk)
    return render(request, 'maestros/detalles_maestro.html', {'maestro': maestro})

@login_required(login_url='/')
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

@login_required(login_url='/')
def agregar_maestro(request):
    if request.method == "POST":
        uform = AgregarUsuario(request.POST,prefix='user')
        upform = AgregarMaestro(request.POST, prefix='userprofile')
        if uform.is_valid() * upform.is_valid():
            user = uform.save()
            maestro = upform.save(commit=False)
            maestro.user = user
            maestro.save()
            return redirect('/maestro/'+str(maestro.pk), pk=maestro.pk)
    else:
        uform = AgregarUsuario(prefix='user')
        upform = AgregarMaestro(prefix='userprofile')
    return render(request, 'base/registrar.html', dict(userform=uform, userprofileform=upform))

@login_required(login_url='/')
def eliminar_maestro(request, pk):
    maestro = Maestro.objects.get(pk=pk)
    maestro.delete()
    maestro = Maestro.objects.all()
    maestro = maestro[::-1]
    return render(request, 'maestros/lista_maestros.html', {'maestros': maestros})
