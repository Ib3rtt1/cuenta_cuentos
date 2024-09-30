# app_cuentos/urls.py

from django.urls import path
from . import views
from .views import agregar_cuento  # Línea de importación corregida

urlpatterns = [
    path('', views.index, name='index'),  # Vista de inicio
    # Vista de lista de cuentos
    path('lista/', views.lista_cuentos, name='lista_cuentos'),
    # Vista para agregar cuentos
    path('agregar/', agregar_cuento, name='agregar_cuento'),
]
