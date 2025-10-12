from rest_framework import serializers
from apps.product.models import Brand,Country


class CountrySerializer (serializers.ModelSerializer) : 

    class Meta : 
        model = Country
        fields = "__all__"

class BrandSerializer (serializers.ModelSerializer) : 

    country = CountrySerializer()

    class Meta : 
        model = Brand
        fields = "__all__"