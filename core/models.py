from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class UserExtension(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    token = models.CharField(max_length=256)
    kontostand = models.IntegerField(default=10000)

class Stock(models.Model):
    wkn = models.CharField(max_length=6)
    name = models.CharField(max_length=128)

class Order(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    action = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Match(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price_sold = models.IntegerField()
    quantity_transaction = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user_buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+',)
    user_seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+',)
