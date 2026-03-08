from django.db import models

# Create your models here.
class ImagenGaleria(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título de la Seña")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='galeria/', verbose_name="Imagen")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Galería de Imágenes"

    def __str__(self):
        return self.titulo