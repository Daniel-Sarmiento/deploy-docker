from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)
    
    class Meta:
        verbose_name_plural = 'Productos'
