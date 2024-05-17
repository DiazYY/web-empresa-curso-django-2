from django.db import models

# Create your models here.
class service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services', null=True, blank=True, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de Creación") # este campo actualiza la fecha de creación
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Modificación") 

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"] # para ordenar desde el mas nuevo al mas antiguo agregar un guion

    def __str__(self):
        return self.title