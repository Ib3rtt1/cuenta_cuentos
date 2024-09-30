from django.db import models

# Create your models here.


class Cuento(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    # Aquí se almacena la ruta del PDF
    archivo_pdf = models.FileField(upload_to='cuentos/', null=True, blank=True)

    def __str__(self):
        return self.titulo
