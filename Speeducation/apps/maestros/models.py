from django.db import models
from django.contrib.auth.models import User
from .choices import choices


# Create your models here.
class Maestro(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='user')
    sexo = models.CharField(max_length=50, choices=choices.GENDER_CHOICES, default=choices.GENDER_CHOICES, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
