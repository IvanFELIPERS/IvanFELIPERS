
import products
from django.db import models

class Category(models.Model):
    name = models.CharField('Categoria', max_length=100)
    description = models.CharField('Descripcion', max_length=200)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Category'
        ordering = ['id']

class Products(models.Model):
    name = models.CharField('Producto', max_length=100)
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2)
    stock = models.IntegerField('Stock')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'product'
        ordering = ['id']


