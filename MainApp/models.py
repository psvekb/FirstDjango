from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    desc = models.CharField(max_length=100, default="Описание товара")
    count = models.PositiveIntegerField()