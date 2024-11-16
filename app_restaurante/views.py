from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ComensalForm
# Create your views here.

def menu_vista(request):
    opciones = ['Comensal', 'Reserva', 'Menu', 'Plato', 'Personal']
    return render(request, 'menu.html', {'opciones': opciones})

def comensal(request):
    if request.method == 'POST':
        form = ComensalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comensal')
    else:
        form = ComensalForm()

    return render(request, 'comensal.html', {'form': form})