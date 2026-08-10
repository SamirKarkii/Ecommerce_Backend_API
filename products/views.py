from django.shortcuts import render
from rest_framework import permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product,Category
from .serializers import CategorySerializer,ProductSerializer
from .permissions import IsAdminOrReadOnly


class ProductView(APIView):
    permission_classes = [IsAdminOrReadOnly]
   

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)


    def post(self,request):  
        
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)

class CategoryView(APIView): 
    permission_classes = [IsAdminOrReadOnly]

    def get(self,request): 
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )