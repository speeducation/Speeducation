from .views import home
from . import views
from django.conf.urls import patterns, include, url

urlpatterns = [
    #url(r'^$', 'apps.maestros.views.home', name='home'),
    url(r'^$', views.login),
    url(r'^maestros/lista/$', views.lista_maestros),
    url(r'^maestro/(?P<pk>[0-9]+)/$', views.detalles_maestro),
    url(r'^maestro/(?P<pk>[0-9]+)/editar/$', views.editar_maestro, name='editar_maestro'),
    url(r'^maestro/agregar/$', views.agregar_maestro, name='agregar_maestro'),
    url(r'^maestro/(?P<pk>[0-9]+)/eliminar/$', views.eliminar_maestro, name='eliminar_maestro')
]
