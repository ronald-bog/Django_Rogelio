from django.db import models

# Modelo para la tabla 'Category'
class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=90)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name



