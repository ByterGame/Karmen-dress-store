from contextlib import nullcontext

from django.db import models


class DressCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Dress(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    color = models.CharField(max_length=256)
    length = models.CharField(max_length=256)
    material = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='products_images')
    photo_hover = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=DressCategory, on_delete=models.CASCADE)
    model = models.CharField(max_length=256)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
