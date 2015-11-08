from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include('apps.maestros.urls'), name='home'),
    url(r'', include('apps.alumnos.urls')),
]
