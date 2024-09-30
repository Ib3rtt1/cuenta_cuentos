from django.db import models

# Create your models here.


class Cuento(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
