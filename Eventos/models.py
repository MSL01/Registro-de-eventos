from django.db import models

class Registro(models.Model):
    nombre_del_evento = models.CharField(null=True, max_length=30)
    tipo_de_evento = models.CharField(null=True, max_length=30)
    desc = models.TextField()
    fecha = models.DateField()
    EST_1 = 'Pendiente por Revisar'
    EST_2 = 'Revisado'
    estado = ((EST_1, u'Pendiente por Revisar'), (EST_2, u'Revisado'))
    est = models.CharField(max_length=22, choices=estado)