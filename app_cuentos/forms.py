# app_cuentos/forms.py

from django import forms
from .models import Cuento


class CuentoForm(forms.ModelForm):
    class Meta:
        model = Cuento
        fields = ['titulo', 'autor', 'archivo_pdf']
