from django.contrib import admin
from apps.product.models import Brand,BrandCountry


@admin.register(Brand)
class BrandAdmin (admin.ModelAdmin) : 
    exclude = ["id","slug"] 

@admin.register(BrandCountry)
class BrandCountryAdmin (admin.ModelAdmin) : 
    exclude = ["id","slug"]