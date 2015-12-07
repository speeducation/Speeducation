from django import forms
from .models import Linea, Actividad, Conducta

class AgregarLinea(forms.ModelForm):
    class Meta:
        model = Linea
        exclude = ['updated']

    def __init__(self, *args, **kwargs):
        super(AgregarLinea, self).__init__(*args,**kwargs)
        self.fields['nombre'].required = True

class AgregarActividad(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['descripcion']
        exclude = ['updated', 'linea']

    def __init__(self, *args, **kwargs):
        super(AgregarActividad, self).__init__(*args,**kwargs)

class AgregarConducta(forms.ModelForm):
    class Meta:
        model = Conducta
        fields = ['descripcion']
        exclude = ['updated', 'linea']

    def __init__(self, *args, **kwargs):
        super(AgregarConducta, self).__init__(*args,**kwargs)
