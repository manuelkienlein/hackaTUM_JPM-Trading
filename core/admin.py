from django.contrib import admin
from django.db import models
from .models import Stock, Order, UserExtension, Match

# Register your models here.
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(UserExtension)
admin.site.register(Match)
