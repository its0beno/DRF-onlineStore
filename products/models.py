from django.db import models


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(stock_quantity__gt=0)


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    decription = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    objects = ProductManager()
