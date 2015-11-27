from django.db import models

from django.utils import timezone
#from durationfield.db.models.fields.duration import DurationField

# Create your models here.
from apps.lineas.models import Conducta, Actividad
from .choices import choices


class Alumno(models.Model):
    nombres =  models.CharField(max_length=50, unique=False)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=50, choices=choices.GENDER_CHOICES, default=choices.GENDER_CHOICES.count(0))
    bio = models.TextField(max_length=500, default="" )
    fecha_registro = models.DateField(blank = False, null = False, default = timezone.now)
    activo = models.BooleanField(default = True)
    maestro = models.CharField(max_length= 50)

    def registrar(self):
        self.fecha_registro = timezone.now()
        self.save()

    def __unicode__(self):
        return self.nombres + ' ' + self.apellidos

class Periodo(models.Model):
    fechaInicio = models.DateField(default=timezone.now())
    fechaFinal = models.DateField(default=timezone.now())

    def __unicode__(self):
        return self.fechaInicio.__str__() + " - " + self.fechaFinal.__str__()


class Evaluacion(models.Model):
    alumno = models.ForeignKey(Alumno)
    actividad = models.ForeignKey(Actividad)
    periodo = models.ForeignKey(Periodo, default="")
    finalizado = models.BooleanField(default=False)
    evaluacionInicial = models.CharField(max_length=20, choices=choices.EVALUATION_CHOICES, default=choices.EVALUATION_CHOICES.count(0))
    evaluacionMedia = models.CharField(max_length=20, choices=choices.EVALUATION_CHOICES, default=choices.EVALUATION_CHOICES.count(0))
    evaluacionFinal = models.CharField(max_length=20, choices=choices.EVALUATION_CHOICES, default=choices.EVALUATION_CHOICES.count(0))

    def __unicode__(self):
        return self.alumno.nombres + " " + self.actividad.__str__()

class Comportamiento(models.Model):
    alumno = models.ForeignKey(Alumno)
    conducta = models.ForeignKey(Conducta)

    def __unicode__(self):
        return self.conducta.__str__()