from django.contrib import admin
from django.db import models
from .models import Stock, Order, Authtoken, Match

# Register your models here.
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(Authtoken)
admin.site.register(Match)
