from django.shortcuts import render, get_object_or_404, redirect
from .models import Loja, Computador
from .forms import LojaForm, ComputadorForm
import random

def dashboard(request):
    # Lógica para salvar nova loja via formulário
    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LojaForm()

    lojas = Loja.objects.all()
    computadores = Computador.objects.all()
    
    # Cálculos para os cards do topo
    total_lojas = lojas.count()
    total_comp = computadores.count()
    migrados = computadores.filter(status='concluido').count()
    
    percentual = (migrados / total_comp * 100) if total_comp > 0 else 0
    
    context = {
        'form': form,
        'total_lojas': total_lojas,
        'percentual': round(percentual, 1),
        'total_comp': total_comp,
        'online': computadores.filter(online=True).count(),
        'offline': computadores.filter(online=False).count(),
        'lojas': lojas,
    }
    return render(request, 'dashboard.html', context)

def detalhe_loja(request, loja_id):
    loja = get_object_or_404(Loja, id=loja_id)

    if request.method == 'POST':
        comp_form = ComputadorForm(request.POST)
        if comp_form.is_valid():
            computador = comp_form.save(commit=False)
            computador.loja = loja  # associa o computador à loja atual
            computador.save()
            return redirect('detalhe_loja', loja_id=loja.id)
    else:
        comp_form = ComputadorForm()

    return render(request, 'detalhe_loja.html', {'loja': loja, 'comp_form': comp_form})

def verificar_status(request, comp_id):
    comp = get_object_or_404(Computador, id=comp_id)
    comp.online = random.choice([True, False]) # Simulação de Ping
    comp.save()
    return redirect('detalhe_loja', loja_id=comp.loja.id)