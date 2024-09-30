from django.shortcuts import render
from .models import Cuento

# Create your views here.


def index(request):
    return render(request, 'app_cuentos/index.html')


def lista_cuentos(request):
    cuentos = Cuento.objects.all()
    return render(request, 'app_cuentos/lista_cuentos.html', {'cuentos': cuentos})
