from django import forms
from .models import Maestro

class AgregarMaestro(forms.ModelForm):

    class Meta:
        model = Maestro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AgregarMaestro, self).__init__(*args,**kwargs)
        self.fields['username'].required = True
        self.fields['nombre'].required = True
        self.fields['apellidos'].required = True
        self.fields['email'].required = True
        self.fields['sexo'].required = True
