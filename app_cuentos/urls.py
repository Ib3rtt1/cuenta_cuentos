#
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.lista_cuentos, name='lista_cuentos'),
]
