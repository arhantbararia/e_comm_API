from django.core.exceptions import ValidationError

from product.models import Product, Brand, Category , ProductLine
from .serializer import ProductSerializer, BrandSerializer , CategorySerializer, ProductLineSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request


class ProductListAV(APIView):

    def get(self , request):


        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)

        return Response(serializer.data)
    
    def post(self , request):
        serializer = ProductSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


class ProductAV(APIView):

    def get_object(self , primaryKey):
        try:
            return Product.object.get(pk = primaryKey)
        
        except Product.DoesNotExist:
            return Response({'ERROR' : 'Object does not exist'}, status = status.HTTP_404_NOT_FOUND)
        
    
    def get(self , request , primaryKey):
        product = self.get_object(primaryKey)
        serializer = ProductSerializer(product)

        return Response(serializer.data)
    

    def put(self , request , primaryKey):
        product = self.get_object(primaryKey )
        serializer = ProductSerializer(product , data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self , request , primaryKey):

        product = self.get_object(primaryKey)

        product.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
    















class BrandListAV(APIView):

    def get(self , request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many = True)

        return Response(serializer.data)
    
    def post(self , request):
        serializer = BrandSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


class BrandAV(APIView):

    def get_object(self , primaryKey):
        try:
            return Brand.object.get(pk = primaryKey)
        
        except Brand.DoesNotExist:
            return Response({'ERROR' : 'Object does not exist'}, status = status.HTTP_404_NOT_FOUND)
        
    
    def get(self , request , primaryKey):
        brand = self.get_object(primaryKey)
        serializer = BrandSerializer(brand)

        return Response(serializer.data)
    

    def put(self , request , primaryKey):
        brand = self.get_object(primaryKey )
        serializer = BrandSerializer(brand , data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self , request , primaryKey):

        brand = self.get_object(primaryKey)

        brand.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
    















class CategoryListAV(APIView):

    def get(self , request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)

        return Response(serializer.data)
    
    def post(self , request):
        serializer = CategorySerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


class CategoryAV(APIView):

    def get_object(self , primaryKey):
        try:
            return Category.object.get(pk = primaryKey)
        
        except Category.DoesNotExist:
            return Response({'ERROR' : 'Object does not exist'}, status = status.HTTP_404_NOT_FOUND)
        
    
    def get(self , request , primaryKey):
        category = self.get_object(primaryKey)
        serializer = CategorySerializer(category)

        return Response(serializer.data)
    

    def put(self , request , primaryKey):
        category = self.get_object(primaryKey )
        serializer = CategorySerializer(category , data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self , request , primaryKey):

        category = self.get_object(primaryKey)

        category.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
    








##########################################################

#             TEST AREA

#######################################################




class TestAV(APIView):
    
    def get(self , request):
        
        print(request)
        print(request.query_params() )

        return Response()


