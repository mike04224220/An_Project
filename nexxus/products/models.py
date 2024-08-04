from django.db import models

class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name='Nombre')  # Nombre del producto
    description = models.TextField(max_length=300, verbose_name='Descripción')  # Descripción del producto
    priceCost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Precio Costo'
    )  # Precio de costo del producto, con precisión decimal
    priceSell = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Precio Venta'
    )  # Precio de venta del producto, con precisión decimal
    available = models.BooleanField(default=True, verbose_name='Disponible')  # Disponibilidad del producto
    units = models.IntegerField(null=True, blank=True, verbose_name='Unidades')  # Unidades disponibles del producto
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name='Foto')  # Foto del producto
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')

    def __str__(self):
        return self.name  # Representación en cadena del producto (nombre)
