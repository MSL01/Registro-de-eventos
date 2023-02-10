from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('Eventos.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
]
