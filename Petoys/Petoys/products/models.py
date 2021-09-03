
from django.db import models

class Products(models.Model):
    name = models.CharField('Producto', max_length=100)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    stock = models.IntegerField('Stock')

    def __str__(self):
        return self.name

