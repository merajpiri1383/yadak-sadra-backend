from rest_framework import serializers
from apps.product.serializers import BrandSerializer,CountrySerializer
from apps.template.models import SlideBox,SlideImage,SliderConfig

class SlideImageSerializer (serializers.ModelSerializer) : 

    class Meta : 
        model = SlideImage
        exclude = ["id","slider"]

class SlideBoxSerializer (serializers.ModelSerializer) : 

    class Meta : 
        model = SlideBox
        exclude = ["id","slider"]

class SliderConfigSerializer (serializers.ModelSerializer) : 

    boxes = SlideBoxSerializer(many=True)

    images = SlideImageSerializer(many=True)

    class Meta : 
        model = SliderConfig
        exclude = ["id"]



class IndexSerializer (serializers.Serializer) : 

    car_brands = BrandSerializer(many=True)

    brand_countries = CountrySerializer(many=True)

    yadak_sadra_brands = BrandSerializer(many=True)

    slider = SliderConfigSerializer()