from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Category, Brand, Product
from .serializer import CategorySerializer, BrandSerializer, ProductSerializer


# Create your views here.


class CategoryViewSet(viewsets.ViewSet):

    queryset = Category.objects.all()

    def list(self, request):
        serialzer = CategorySerializer(self.queryset , many = True)

        return Response(serialzer.data)
    


class BrandViewSet(viewsets.ViewSet):

    queryset = Brand.objects.all()

    def list(self, request):
        serialzer = BrandSerializer(self.queryset , many = True)

        return Response(serialzer.data)
    

class ProductViewSet(viewsets.ViewSet):

    queryset = Product.objects.all()

    def list(self, request):
        serialzer = ProductSerializer(self.queryset , many = True)

        return Response(serialzer.data)
    
