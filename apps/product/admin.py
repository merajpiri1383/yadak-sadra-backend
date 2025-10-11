from django.contrib import admin
from apps.product.models import Brand,Country


@admin.register(Brand)
class BrandAdmin (admin.ModelAdmin) : 
    exclude = ["id","slug"] 

@admin.register(Country)
class CountryAdmin (admin.ModelAdmin) : 
    exclude = ["id","slug"]