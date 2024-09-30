#

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Vista de inicio
    # Vista de lista de cuentos
    path('lista/', views.lista_cuentos, name='lista_cuentos'),
]
