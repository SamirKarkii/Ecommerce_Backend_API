from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product,Category
from .serializers import CategorySerializer,ProductSerializer
from .permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from django.db.models.deletion import ProtectedError


class ProductView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        products = Product.objects.filter(is_active=True)
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
    
class ProductDetailView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        product = get_object_or_404(Product,pk=pk, is_active=True)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(
         instance= product,
        data=request.data,
        partial=True )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk): 
        product = get_object_or_404(Product,pk=pk)
        product.is_active=False
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryDetailView(APIView): 
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request,pk): 
        category = get_object_or_404(Category,pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def patch(self,request,pk): 
        category = get_object_or_404(Category,pk=pk)
        serializer = CategorySerializer(instance=category,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request,pk): 
        category = get_object_or_404(Category,pk=pk)
        try: 
            category.delete()
        except ProtectedError: 
            return Response({"detail": "Cannot delete this category because products are still using it."},status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_204_NO_CONTENT)