from django import forms
from .models import comensal
from .models import mesa

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

class MesaForm(forms.ModelForm):
    class Meta:
        model = mesa
        fields = ['capacidad', 'estado_mesa']
        widgets = {
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Capacidad'}),
            'estado_mesa': forms.Select(choices=[
                ('libre', 'Libre'),
                ('ocupada', 'Ocupada'),
                ('en_reserva', 'En Reserva')
            ], attrs={'class': 'form-control'}),
        }