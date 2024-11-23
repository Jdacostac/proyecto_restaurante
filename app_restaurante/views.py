from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ComensalForm
from .models import comensal
from .models import mesa
from .forms import MesaForm
from .forms import ReservaForm
from .models import reserva

# Create your views here.

def menu_vista(request):
    opciones = ['Comensal', 'Mesa', 'Personal', 'Plato']
    return render(request, 'menu.html', {'opciones': opciones})

def registro_comensal(request):
    if request.method == 'POST':
        form = ComensalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_comensal')
    else:
        form = ComensalForm()

    return render(request, 'registro_comensal.html', {'form': form})

def listar_comensales(request):
    comensales = comensal.objects.all() 
    return render(request, 'listar_comensales.html', {'comensales': comensales})

def registrar_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_mesa')
    else:
        form = MesaForm()

    return render(request, 'registrar_mesa.html', {'form': form})

def listar_mesas(request):
    mesas = mesa.objects.all()  
    return render(request, 'listar_mesas.html', {'mesas': mesas})


def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('listar_reservas') 
    else:
        form = ReservaForm()

    return render(request, 'crear_reserva.html', {'form': form})

def listar_reservas(request):
    reservas = reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})