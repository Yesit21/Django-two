from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    fecha_solicitud = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Solicitud
        fields = [
            'nombre_solicitante',
            'documento',
            'email',
            'telefono',
            'tipo_solicitud',
            'asunto',
            'descripcion',
            'fecha_solicitud',
            'archivo_adj',
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }
