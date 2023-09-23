from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.exceptions import ValidationError
# Create your models here.

from .fields import OrderField


class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)




class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    objects = ActiveQueryset.as_manager()

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
    

    def __str__(self):
        return self.name


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
    
    attribute_value = models.ManyToManyField(AttributeValue)

    def clean(self):
        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate value.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLine, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.sku)




class ProductImage(models.Model):
    
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(upload_to=None ,default = "test.jpg")

    product = models.ForeignKey(
        ProductLine, on_delete = models.CASCADE, related_name = 'product_image'
    )
    
    
    def __str__(self):
        return str(self.url)
    


