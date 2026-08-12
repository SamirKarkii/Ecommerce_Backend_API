from rest_framework import serializers
from .models import Cart,CartItem

class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1)

    class Meta: 
        model = CartItem
        fields = ["id","product","quantity"]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True )  #cart.items.all()
 
    class Meta:
        model = Cart
        fields = ["id", "items"]

