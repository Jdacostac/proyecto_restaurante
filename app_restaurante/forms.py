from django import forms
from .models import comensal
from .models import mesa
from .models import reserva, comensal, mesa
from django.forms.widgets import DateTimeInput

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

class ReservaForm(forms.ModelForm):
    class Meta:
        model = reserva
        fields = ['cedula_comensal', 'num_mesa', 'fecha_reserva', 'num_personas', 'estado']

    cedula_comensal = forms.ModelChoiceField(
        queryset=comensal.objects.all(),
        to_field_name='nombre',
        empty_label="Seleccione un Comensal",
        label="Comensal"
    )

    num_mesa = forms.ModelChoiceField(
        queryset=mesa.objects.filter(estado_mesa__in=['libre']),
        to_field_name='num_mesa',
        empty_label="Seleccione una Mesa",
        label="Mesa"
    )

    fecha_reserva = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Fecha y Hora de Reserva",
        input_formats=['%Y-%m-%dT%H:%M']
    )

    estado = forms.ChoiceField(
        choices=[('en reserva', 'En Reserva'), ('liberada', 'Liberada')],
        widget=forms.Select,
        label="Estado de la Reserva"
    )