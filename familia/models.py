from django.db import models

from concurrent.futures.process import _MAX_WINDOWS_WORKERS


class individuo(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)

class hi(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)