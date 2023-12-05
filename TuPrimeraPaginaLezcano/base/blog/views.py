from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Entrada
from .forms import EntradaForm, BusquedaForm

def listar_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'blog/listar_entradas.html', {'entradas': entradas})

def agregar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_entradas')
    else:
        form = EntradaForm()
    return render(request, 'blog/agregar_entrada.html', {'form': form})

def buscar_entrada(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            resultados = Entrada.objects.filter(Q(titulo__icontains=busqueda) | Q(contenido__icontains=busqueda))
            return render(request, 'blog/buscar_entrada.html', {'resultados': resultados, 'form': form})
    else:
        form = BusquedaForm()
    return render(request, 'blog/buscar_entrada.html', {'form': form})