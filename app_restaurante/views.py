from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComensalForm
from .models import comensal
from .models import mesa
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

def eliminar_comensal(request, cedula):
    comensal_a_eliminar = get_object_or_404(comensal, cedula=cedula)
    comensal_a_eliminar.delete()
    return redirect('listar_comensales')

from django.shortcuts import render, redirect
from .forms import MesaForm

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