from rest_framework.response import Response
from .serializers import CartSerializer,CartItemSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from .models import CartItem,Cart
from rest_framework import status

class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request): 
        cart,_ = Cart.objects.get_or_create(user=request.user) #try cart else create cart 
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    def post(self, request): 
        cart, _ = Cart.objects.get_or_create(user=request.user) #ik this creates or gets the existing cart 
        serializer = CartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    #basically, using validated_data than raw request.data,because drf has already checked that the product exists and quantity is valid
        product = serializer.validated_data["product"]
        quantity = serializer.validated_data["quantity"]
        cart_item,created = CartItem.objects.get_or_create(cart=cart,product=product,defaults={"quantity":quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            output_serializer = CartItemSerializer(cart_item)
            return Response(
        output_serializer.data,
        status=status.HTTP_200_OK
    )


