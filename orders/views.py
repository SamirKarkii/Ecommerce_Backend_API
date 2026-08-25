from .models import Order,OrderItem
from rest_framework.response import Response
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from cart.models import Cart
from rest_framework import status
from django.db import transaction
from products.models import Product

# class OrderView(APIView): 
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request): 
#         order = Order.objects.filter(user=request.user)
#         serializer= OrderSerializer(order,many=True)
#         return Response(serializer.data)

# # Create your views here.
#     def post(self,request): 
#         cart = get_object_or_404(Cart,user=request.user)
#         cart_items = cart.items.all()
#         if not cart_items.exists():
#             return Response({"detail":"Cart is empty."},status=status.HTTP_400_BAD_REQUEST)

#         for cart_item in cart_items:
#             product = cart_item.product
#             if not product.is_active:
#                 return Response( {"detail": f"{product.name} is not available."}, status=status.HTTP_400_BAD_REQUEST   )
#             if cart_item.quantity > product.stock:
#                     return Response( {"detail": f"Insufficient stock for {product.name}."},   status=status.HTTP_400_BAD_REQUEST )

#         order = Order.objects.create(user=request.user)
#         total = 0
#         for cart_item in cart_items:
#              product = cart_item.product
#              product_name =product.name
#              unit_price = product.price
#              quantity=cart_item.quantity

#              OrderItem.objects.create(order=order,product=product,product_name=product_name,unit_price=unit_price,quantity=quantity)
#              total += unit_price * quantity
#              product.stock = product.stock-quantity
#              product.save()
#         order.total_amount = total
#         order.save()
#         cart_items.delete()

#         serializer = OrderSerializer(order)
#         # serializer.save() #bro we created ourself so the db saves it 
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


class OrderView(APIView): 
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request): 
        order = Order.objects.filter(user=request.user)
        serializer= OrderSerializer(order,many=True)
        return Response(serializer.data)

    def post(self,request): 
        cart = get_object_or_404(Cart,user=request.user)
        cart_items = cart.items.all()
        if not cart_items.exists():
            return Response({"detail":"Cart is empty."},status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
             locked_items=[]
             for cart_item in cart_items:
                 product = Product.objects.select_for_update().get(id=cart_item.product_id)

                 if not product.is_active:
                  return Response(  {"detail": f"{product.name} is not available."},   status=status.HTTP_400_BAD_REQUEST)

                 if cart_item.quantity > product.stock:return Response({"detail": f"Insufficient stock for {product.name}."},
                status=status.HTTP_400_BAD_REQUEST)

                 locked_items.append((cart_item, product))

                 #if every thing pass , then create order 
             order = Order.objects.create(user=request.user)
             total = 0
             for cart_item,product in locked_items:
                 OrderItem.objects.create(order=order,product=product, product_name=product.name,unit_price=product.price,quantity=cart_item.quantity)
                 total += product.price * cart_item.quantity
                 product.stock -= cart_item.quantity
                 product.save()

             order.total_amount = total
             order.save()
             cart_items.delete()

             serializer = OrderSerializer(order)
             return Response(serializer.data,status=status.HTTP_201_CREATED)



                 



                 
            
        
            
