from django.core.exceptions import ValidationError
from django.db import connection

from product.models import Product, Brand, Category , ProductLine
from .serializer import ProductSerializer, BrandSerializer , CategorySerializer, ProductLineSerializer

from rest_framework.response import Response
from django.db.models import Prefetch

from rest_framework.views import APIView
from rest_framework import status


class ProductListAV(APIView):

    def get(self , request):

        if(len(request.query_params) == 0):
            products = Product.objects.all()
        elif('category' in request.query_params ):
            products = Product.objects.filter(category__name = request.query_params['category']  )
        elif('search' in request.query_params):
            products = Product.objects.filter(slug= request.query_params['search'])
        
        serializer = ProductSerializer(products.select_related("category" , "brand")
                                       .prefetch_related(Prefetch("product_line"))
                                        .prefetch_related(Prefetch("product_line__product_image"))
                                        .prefetch_related(Prefetch("product_line__attribute_value__attribute")) , many = True)
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
            return Product.objects.get(pk = primaryKey)
        
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
            return Brand.objects.get(pk = primaryKey)
        
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
            return Category.objects.get(pk = primaryKey)
        
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
        
      
        

        products = Product.objects.all()
        serializer = ProductSerializer(products.select_related("category" , "brand")
                                       .prefetch_related(Prefetch("product_line"))
                                        .prefetch_related(Prefetch("product_line__product_image"))
                                        .prefetch_related(Prefetch("product_line__attribute_value__attribute")) , many = True)
        data = serializer.data
        
        qs = list(connection.queries)
        
        # for q in qs:

        #     print(q)

        
        print(len(qs))


        return Response(data)



