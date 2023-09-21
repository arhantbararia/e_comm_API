from django.urls import path

from .views import *



urlpatterns = [
    path("products/", ProductListAV.as_view() , name = 'Product-list'),
    path('product/<int:primaryKey>' ,  ProductAV.as_view() , name = 'Product-detail'),

    path('brands/' , BrandListAV.as_view(), name= 'brands-list'),
    path('brand/<int:primarykey>' , BrandAV.as_view(), name = 'brand-detail'),
    
    path('categories/' , CategoryListAV.as_view(), name = 'category-list'),
    path('category/<int:primaryKey' , CategoryAV.as_view() , name= 'Category-detail'),

    path('test/' , TestAV.as_view(), name= 'Testing area')
]

