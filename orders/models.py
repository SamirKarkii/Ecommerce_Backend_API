from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="orders")
    status = models.CharField(max_length=20,default="pending")
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name="order_items")
    product_name= models.CharField(max_length=200)
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
   