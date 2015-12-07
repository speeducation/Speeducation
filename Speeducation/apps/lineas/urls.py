from . import views
from django.conf.urls import patterns, include, url

urlpatterns = [
    #LINEA
    url(r'^lineas/lista/$', views.lista_lineas),
    url(r'^linea/(?P<pk>[0-9]+)/editar/$', views.editar_linea, name='editar_linea'),
    url(r'^lineas/agregar/$', views.agregar_linea, name='agregar_linea'),
    url(r'^linea/(?P<pk>[0-9]+)/eliminar/$', views.eliminar_linea, name='eliminar_linea'),
    url(r'^linea/(?P<pk>[0-9]+)/$', views.detalles_linea, name='detalles_linea'),
    #ACTIVIDAD,
    url(r'^linea/([0-9]\d+)/actividad/(?P<pk>[0-9]+)/editar$', views.editar_actividad, name='editar_actividad'),
    url(r'^linea/([0-9]\d+)/actividad/(?P<pk>[0-9]+)/eliminar', views.eliminar_actividad, name='eliminar_actividad'),
    url(r'^linea/(?P<pk>[0-9]+)/actividad/agregar/$', views.agregar_actividad, name='agregar_actividad'),
    #CONDUCTA
    url(r'^linea/([0-9]\d+)/conducta/(?P<pk>[0-9]+)/editar$', views.editar_conducta, name='editar_conducta'),
    url(r'^linea/([0-9]\d+)/conducta/(?P<pk>[0-9]+)/eliminar', views.eliminar_conducta, name='eliminar_conducta'),
    url(r'^linea/(?P<pk>[0-9]+)/conducta/agregar/$', views.agregar_conducta, name='agregar_conducta'),
    #PLAN DE ESTUDIO
    #url(r'^linea/actividad/(?P<pk>[0-9]+)/editar/$', views.editar_linea, name='editar_linea_actividad'),
    #url(r'^linea/actividad/agregar$', views.agregar_linea_actividad, name='agregar_linea_actividad'),
    #url(r'^lineas/actividad/(?P<pk>[0-9]+)/eliminar/$', views.eliminar_maestro, name='eliminar_maestro'),
]
