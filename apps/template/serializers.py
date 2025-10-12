from rest_framework import serializers
from apps.product.serializers import BrandSerializer,CountrySerializer



class IndexSerializer (serializers.Serializer) : 

    car_brands = BrandSerializer(many=True)

    brand_countries = CountrySerializer(many=True)

    yadak_sadra_brands = BrandSerializer(many=True)