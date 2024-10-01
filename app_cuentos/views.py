from django.shortcuts import render, redirect, get_object_or_404
from .forms import CuentoForm
from .models import Cuento

# Create your views here.


def index(request):
    cuentos = Cuento.objects.all()  # Obtén todos los cuentos
    return render(request, 'app_cuentos/index.html', {'cuentos': cuentos})


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


def ver_pdf(request, id):
    cuento = get_object_or_404(Cuento, id=id)
    return render(request, 'app_cuentos/ver_pdf.html', {'cuento': cuento})
