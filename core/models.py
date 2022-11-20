from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserExtension(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    token = models.CharField(max_length=256)
    kontostand = models.IntegerField(default=10000)

    def __str__(self):
        return self.user.get_full_name()

class Stock(models.Model):
    wkn = models.CharField(max_length=6)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name + " (" + self.wkn + ")"

class Order(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
