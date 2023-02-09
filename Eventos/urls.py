from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.ViewPost.as_view(), name='posts'),
]