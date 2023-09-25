from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Product , Brand, Category, ProductLine, ProductImage, AttributeValue , Attribute , ProductType

class EditLinkInLine(object):
    def edit(self , instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk]
        )
        

        if instance.pk:
            link = mark_safe('<a href="{u}">edit</a>'.format(u=url))
            return link
        else:
            return ""
        
class AttributeInLine(admin.TabularInline):
    model = Attribute.product_type_attribute

class ProductImageInLine(admin.TabularInline):
    model = ProductImage


class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInLine,
    ]



class ProductLineInLine(EditLinkInLine, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit" , )


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInLine]





admin.site.register(ProductLine , ProductLineAdmin )
admin.site.register(Product , ProductAdmin)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(AttributeValue)
admin.site.register(Attribute)



