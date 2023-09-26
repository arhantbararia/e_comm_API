from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.exceptions import ValidationError
# Create your models here.
from datetime import datetime
from .fields import OrderField



### Class to filter inactive objects
class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)




class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    objects = ActiveQueryset.as_manager()
    created_at = models.DateTimeField(auto_now_add=True , editable = False)
    updated = models.DateTimeField(auto_now= True , editable = True)


    class Meta:
        verbose_name= "Category"
        verbose_name_plural = "Categories"

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    objects = ActiveQueryset.as_manager()
    created_at = models.DateTimeField(auto_now_add=True , editable = False)
    updated = models.DateTimeField(auto_now= True , editable = True)

    

    def __str__(self):
        return self.name





class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True )
    

   
    def __str__(self) -> str:
        return self.name




class AttributeValue(models.Model):
    att_value = models.CharField(max_length=100)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name= "attribute_value", null = True 
    )
    

    def __str__(self) -> str:
        return f"{self.attribute.name}-{self.att_value}"





class ProductType(models.Model):
    name = models.CharField(max_length= 100)
    

    def NOT_SET():                              #SETS THE DEFAULT ATTRIBUTE TO NOT SET
        not_set_attribute = Attribute.objects.filter(pk = 3)
        return not_set_attribute
    
    attribute = models.ManyToManyField(Attribute ,related_name="product_type_attribute", default = NOT_SET )

    @classmethod
    def get_default_pk(cls):
        product_type, created = cls.objects.get_or_create(
            name = "Potato",
            
        )
        return product_type.pk

    def __str__(self):
        return str(self.name)



class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null = True , blank= True
    )
    is_active = models.BooleanField(default=False)
    
    objects = ActiveQueryset.as_manager()
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT , default=ProductType.get_default_pk)
    created_at = models.DateTimeField(auto_now_add=True , editable = False)
    updated = models.DateTimeField(auto_now= True , editable = True)


    def __str__(self):
        return self.name


def select_attribute_value_of_product_type(instance):
    product_attributes = instance.product.product_type.attribute.all()
    print(instance.id)
    selected_attributes = [attr_value.attribute for attr_value in instance.attribute_value.all()]

    print(product_attributes)
    print(selected_attributes)

    for attribute in selected_attributes:
        print(attribute)
        if attribute not in product_attributes:
            raise ValidationError(
                f"The attribute '{attribute.name}' is not allowed in for the selected product type."
                )
        

def validate_single_attribute_value(instance):
    # Get the attribute values associated with this product line
    attribute_values_count = {}

        # Iterate through the attribute values associated with this product line
    for attribute_value in instance.attribute_value.all():
        attribute = attribute_value.attribute

            # Check if the attribute already has an associated value
        if attribute in attribute_values_count:
            raise ValidationError(
                f"Only one attribute value is allowed for attribute '{attribute.name}'."
            )
        else:
            attribute_values_count[attribute] = attribute_value


class ProductLine(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField(default = 0   )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    is_active = models.BooleanField(default=False)

    order = OrderField(unique_for_field="product" , default = 0 ,blank = True) #####################needs to be looked at

    objects = ActiveQueryset.as_manager()
    
    attribute_value = models.ManyToManyField(AttributeValue, blank= True )
    #product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT , default=ProductType.get_default_pk)
    created_at = models.DateTimeField(auto_now_add=True , editable = False)
    updated = models.DateTimeField(auto_now= True , editable = True)

    
    def clean(self):
        print("cleaned!")

         # Check if there are duplicate attributes in attribute_value
        

        super().clean()
        #validate_single_attribute_value(self)
        
      
    def save(self, *args, **kwargs):

        self.full_clean()
        super(ProductLine, self).save(*args, **kwargs)
        #select_attribute_value_of_product_type(self)
        print("saved!")
        


    def __str__(self):
        return str(self.sku)




class ProductImage(models.Model):
    
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None ,default = "test.jpg")

    product = models.ForeignKey(
        ProductLine, on_delete = models.CASCADE, related_name = 'product_image'
    )
    updated = models.DateTimeField(auto_now= True )
    
    
    def __str__(self):
        return str(self.url)
    


