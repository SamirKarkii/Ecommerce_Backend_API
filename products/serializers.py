from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields= ["id","name"]

class ProductSerializer(serializers.ModelSerializer):
     price = serializers.DecimalField( max_digits=10, decimal_places=2,  min_value=0)
     class Meta: 
        model = Product
        fields = [ "id",
            "name",
            "description",
            "price",
            "stock",
            "category",
            "is_active",
            "created_at",
            "updated_at",]