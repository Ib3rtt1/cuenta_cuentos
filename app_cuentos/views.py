from django.shortcuts import render, redirect
from .forms import CuentoForm
from .models import Cuento


# Create your views here.


def index(request):
    return render(request, 'app_cuentos/index.html')


def lista_cuentos(request):
    cuentos = Cuento.objects.all()
    return render(request, 'app_cuentos/lista_cuentos.html', {'cuentos': cuentos})


def agregar_cuento(request):
    if request.method == 'POST':
        form = CuentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirige a la vista de lista de cuentos
            return redirect('lista_cuentos')
    else:
        form = CuentoForm()
    return render(request, 'app_cuentos/agregar_cuento.html', {'form': form})
