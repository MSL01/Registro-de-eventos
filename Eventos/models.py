from django.db import models

class Registro(models.Model):
    event_name = models.CharField(null=True, max_length=30)
    event_type = models.CharField(null=True, max_length=30)
    desc = models.TextField()