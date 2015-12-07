from time import timezone

from django.db import models

class Linea(models.Model):
    class meta:
        verbose_name_plural = "Lineas"

    nombre =  models.CharField(max_length=50, unique=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.nombre

class Conducta(models.Model):
    class meta:
        verbose_name_plural = "Conductas"

    descripcion =  models.CharField(max_length=75, unique=True)
    linea = models.ForeignKey('Linea')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.descripcion

class Actividad(models.Model):
    class meta:
        verbose_name_plural = "Actividades"

    descripcion =  models.CharField(max_length=75, unique=True)
    linea = models.ForeignKey('Linea')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.descripcion