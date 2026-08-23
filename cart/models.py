from django.db import models
from django.conf import settings
from products.models import Product
  

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="cart")

    def __str__(self):
        return f"Cart of {self.user.email}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product =models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    class Meta:   #UNIQUE (cart_id, product_id) #It does not create a second cart item because you also have this database rule
        constraints = [
        models.UniqueConstraint(
            fields=["cart", "product"],
            name="unique_product_per_cart"
        )
    ]
