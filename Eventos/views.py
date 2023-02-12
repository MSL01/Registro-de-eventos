from django.shortcuts import render, redirect
from django.views import generic
from .models import Registro
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound

class ViewPost(generic.ListView):
    template_name = 'Eventos/posts.html'
    model = Registro

def crear(request):
    if request.method == 'post':
        fecha = request.POST.get('fecha')
        desc = request.POST.get('desc')
        data = Registro(fecha=fecha, desc=desc)
        data.save()
    return render(request, 'Eventos/crear.html', {'form': data})

def editdata(request, idd):
    get_data = Registro.objects.get(id=idd)
    return render(request, 'Eventos/edit.html', {'key2': get_data})

def updatedata(request, idd):
    upddata = Registro.objects.get(id=idd)
    upddata.nombre_del_evento = request.POST['nameev']
    upddata.tipo_de_evento = request.POST['tipoev']
    upddata.desc = request.POST['descev']
    upddata.fecha = request.POST['fechaev']
    upddata.est = request.POST['estev']
    upddata.gestion = request.POST['gestev']
    upddata.save()
    return redirect('home')

def deletedata(request, idd):
    data = Registro.objects.get(id=idd)
    data.delete()
    return redirect('home')
class WritePost(generic.CreateView):
    template_name = 'Eventos/crear.html'
    model = Registro
    fields = ['nombre_del_evento', 'tipo_de_evento', 'desc', 'fecha']

    def get_initial(self,):
        initial = super().get_initial()
        return initial

class Administracion(generic.ListView):
    template_name = 'Eventos/admin.html'
    model = Registro