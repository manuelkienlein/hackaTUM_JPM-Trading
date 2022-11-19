from django.db.models import fields
from rest_framework import serializers
from core.models import Stock

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('wkn', 'name')