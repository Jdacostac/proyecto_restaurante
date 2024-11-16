from django import forms
from .models import comensal

class ComensalForm(forms.ModelForm):
    class Meta:
        model = comensal
        fields = ['cedula', 'nombre', 'telefono', 'correo']
        widgets = {
            'cedula': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su cédula'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre'
            }),
            'telefono': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su teléfono'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su correo electrónico'
            }),
        }