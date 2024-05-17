from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación") # este campo actualiza la fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Modificación")

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["name"] # para ordenar desde el mas nuevo al mas antiguo agregar un guion

    def __str__(self):
        return self.name
