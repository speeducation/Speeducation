from django.db import models

from django.utils import timezone
#from durationfield.db.models.fields.duration import DurationField

# Create your models here.
class Alumno(models.Model):

    nombres =  models.CharField(max_length=50, unique=False)
    apellidos = models.CharField(max_length=100)
    fecha_registro = models.DateField(blank = False, null = False, default = timezone.now())
    grupo = models.IntegerField()
    activo = models.BooleanField(default = True)
    maestro = models.CharField(max_length= 50)

    def registrar(self):
        self.fecha_registro = timezone.now()
        self.save()

    def __unicode__(self):
        return self.nombres + ' ' + self.apellidos
