from django.db import models

class Category(models.Model): 
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name 

class Product(models.Model): 
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True) #created_at stays the same time 
    updated_at = models.DateTimeField(auto_now=True) #update this date/time every time this object is saved . 

    def __str__(self):
        return self.name
