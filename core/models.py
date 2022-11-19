from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Authtoken(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    token = models.CharField(max_length=256)

class Stock(models.Model):
    wkn = models.CharField(max_length=6)
    name = models.CharField(max_length=128)

class Order(models.Model):
    
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    action = models.BooleanField()
    
    
       
