from django.urls import re_path as url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.ViewPost.as_view(), name='home'),
    url(r'^crear_registro/$', views.WritePost.as_view(success_url='/'), name='crear'),
    url(r'^administracion/$', views.Administracion.as_view(), name='admin'),
    path('delete/<int:idd>/', views.deletedata, name='delete'),
    path('editdata/<int:idd>/', views.editdata, name='edit'),
    path('updatedata/<int:idd>/', views.updatedata, name='update'),
]