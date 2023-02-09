from django.shortcuts import render
from django.views import generic
from .models import Registro


class ViewPost(generic.ListView):
    template_name = 'Eventos/posts.html'
    model = Registro