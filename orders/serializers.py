from .models import Order,OrderItem
from rest_framework import serializers


class OrderItemSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = OrderItem
        fields = ["id","product","product_name","unit_price","quantity"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    class Meta: 
        model = Order
        fields = ["id","status","total_amount","created_at","items"]

