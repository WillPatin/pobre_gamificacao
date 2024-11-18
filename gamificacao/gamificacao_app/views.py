from django.shortcuts import render, redirect
from .models import Selo
from .forms import SeloForm

def listar_selos(request):
    selos = Selo.objects.all()
    return render(request, 'listar_selos.html', {'selos': selos})

def adicionar_selo(request):
    if request.method == 'POST':
        form = SeloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_selos')
    else:
        form = SeloForm()
    return render(request, 'adicionar_selo.html', {'form': form})
