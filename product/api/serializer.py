from rest_framework import serializers

from product.models import Brand, Category , Product, ProductLine, ProductImage, Attribute , AttributeValue






class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ("__all__")


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()
    class Meta:
        model = AttributeValue
        fields = ("id" , "att_value" , "attribute")





class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id" , "url")







class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="name")

    class Meta:
        model = Category
        fields = ["category_name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("id",)


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many = True)
    attribute_value = AttributeValueSerializer(many = True)
    class Meta:
        model = ProductLine
        fields = (
            "price",
            "sku",
            "product_image",
            "attribute_value"
        )


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "product_line",
        )