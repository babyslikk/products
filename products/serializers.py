from itertools import product
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Product
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity']