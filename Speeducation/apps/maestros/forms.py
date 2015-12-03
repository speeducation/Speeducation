from django import forms
from .models import Maestro
from django.contrib.auth.models import User

class AgregarUsuario(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['groups','is_superuser','last_login', 'user_permissions','last_login','date_joined']

class AgregarMaestro(forms.ModelForm):
    class Meta:
        model = Maestro
        exclude = ['user']
