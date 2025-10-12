from django.contrib import admin
from apps.product.models import Brand,Country,Product,ProductImage



@admin.register(Brand)
class BrandAdmin (admin.ModelAdmin) : 
    exclude = ["id","slug"] 

@admin.register(Country)
class CountryAdmin (admin.ModelAdmin) : 
    exclude = ["id","slug"]


class ProductImageInline (admin.TabularInline) : 
    model = ProductImage
    extra = 0
    exclude = ["id"]

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin) : 
    exclude = ['id',"slug"]
    inlines = [ProductImageInline]