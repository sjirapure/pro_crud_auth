from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptop_id = models.IntegerField()
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    ram = models.CharField(max_length=20)
    rom = models.CharField(max_length=20)
    HDD = models.CharField(max_length=30)
    SSD = models.CharField(max_length=30)
    price = models.FloatField()