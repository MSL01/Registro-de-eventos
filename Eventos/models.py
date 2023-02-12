from django.db import models
from django import forms


class Registro(models.Model):
    nombre_del_evento = models.CharField(null=True, max_length=30)
    tipo_de_evento = models.CharField(null=True, max_length=30)
    desc = models.TextField()
    fecha = models.DateField()
    est = models.CharField(max_length=22, default='Pendiente por Revisar')
    gestion = models.CharField(max_length=22, default='Pendiente por Revisar')
