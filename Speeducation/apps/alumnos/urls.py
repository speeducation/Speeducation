from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.lista_alumnos),
    url(r'^alumno/(?P<pk>[0-9]+)/$', views.detalles_alumno),
    url(r'^alumno/(?P<pk>[0-9]+)/editar/$', views.editar_alumno, name='editar_alumno'),
    url(r'^alumno/agregar/$', views.agregar_alumno, name='agregar_alumno'),
]
