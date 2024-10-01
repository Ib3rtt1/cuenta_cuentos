# app_cuentos/urls.py

from django.urls import path
from . import views
from .views import agregar_cuento  # Línea de importación corregida

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),  # Vista de inicio
    # Vista de lista de cuentos
    path('lista/', views.lista_cuentos, name='lista_cuentos'),
    # Vista para agregar cuentos
    path('agregar/', agregar_cuento, name='agregar_cuento'),
    path('ver_pdf/<int:id>/', views.ver_pdf, name='ver_pdf'),  # Nueva ruta
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Esto agrega las rutas para servir archivos multimedia (como los PDFs)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
