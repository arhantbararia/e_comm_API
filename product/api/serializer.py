from rest_framework import serializers

from product.models import Brand, Category , Product, ProductLine, ProductImage, Attribute , AttributeValue, ProductType






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





class ProductTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductType
        fields = ("name",)





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
            "id",
            "price",
            "sku",
            "product_image",
            "attribute_value",
            
        )
    

    def to_representation(self, instance):                      ##### good hack

        data = super().to_representation(instance)    
        # print(1)
        # print(data)            #1
        # print("\n\n\n\n\n")
        av_data = data.pop("attribute_value")
        # print(2)
        # print(av_data) 
        # print("\n\n\n\n\n")
        # print(3)             
        # print(data)
        # print("\n\n\n\n\n")
        # i = 3
        attr_values = {       }
        for key in av_data:
            # print(i +  1 )
            # i += 1
            # print(key)
            attr_values.update({key["attribute"]["name"] : key["att_value"]})

        # print(i)
        # i += 1
        # print(attr_values)



        # print(i)
        # i += 1
        data.update({"specification" : attr_values})
        # print(data)

        
        return data


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True)
    attribute = serializers.SerializerMethodField()
    product_type = ProductTypeSerializer()


    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "description",
            "brand_name",
            "category_name",
            "product_line",
            "product_type",
            "attribute",
            
        )
    

    def get_attribute(self, instance):
       attribute = Attribute.objects.filter(product_type_attribute__product__id = instance.id)
       print("all good here!")
       return AttributeSerializer(attribute, many = True).data
    


    
    def to_representation(self, instance):                      ##### good hack

        data = super().to_representation(instance)    
        print(1)
        print(data)            #1
        print("\n\n\n\n\n")
        av_data = data.pop("attribute")
        print(2)
        print(av_data) 
        print("\n\n\n\n\n")
        print(3)             
        print(data)
        print("\n\n\n\n\n")
        i = 3
        attr_names = {       }
        for key in av_data:
            print(i +  1 )
            i += 1
            print(key)
            attr_names.update({key["id"] : key["name"]})
            print(attr_names)

        print(i)
        i += 1
        print(attr_names)



        print(i)
        i += 1
        data.update({"type specification" : attr_names})
        print(data)

        
        return data
