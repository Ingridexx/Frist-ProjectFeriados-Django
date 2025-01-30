# Aqui vai definir forms para criar e editar instâcias do Holiday através da interface de usuário

from django import forms 
from .models import Holiday

class HolidayForm(form.ModelForm):
    class Meta:
        model = Holiday
        fields = ['nome', 'data', 'tipo']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }