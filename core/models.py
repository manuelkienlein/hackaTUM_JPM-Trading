from django.conf import settings
from django.db import models

class Stock(models.Model):
    wkn = models.CharField(max_length=6)
    name = models.CharField(max_length=128)

class Order(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    action = models.BooleanField()
