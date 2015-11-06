from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', 'apps.dashboard.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
