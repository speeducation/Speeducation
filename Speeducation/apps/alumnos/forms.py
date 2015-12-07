from django import forms
from .models import Alumno, PlanEstudio
from apps.maestros.models import Maestro

class AgregarAlumno(forms.ModelForm):

    class Meta:
        model = Alumno
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AgregarAlumno, self).__init__(*args,**kwargs)
        self.fields['nombres'].required = True
        self.fields['apellidos'].required = True
        self.fields['fecha_registro'].required = True
        self.fields['grupo'].required = True
        self.fields['activo'].required = True
        self.fields['maestro'].required = True
    maestro = forms.ModelChoiceField(queryset=Maestro.objects.all())

class AgregarPlan(forms.ModelForm):
    class Meta:
        model = PlanEstudio
        fields = ['linea', 'periodo']
        exclude = ['alumno']

    def __init__(self, *args, **kwargs):
        super(AgregarPlan, self).__init__(*args,**kwargs)
