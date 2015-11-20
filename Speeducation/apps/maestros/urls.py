from .views import home
from . import views
from django.conf.urls import patterns, include, url

urlpatterns = [
    #url(r'^$', 'apps.maestros.views.home', name='home'),
    url(r'^maestros/lista/$', views.lista_maestros),
]
