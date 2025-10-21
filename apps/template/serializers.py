from rest_framework import serializers
from apps.product.serializers import BrandSerializer,CountrySerializer
from apps.template.models import (
    SlideBox,SlideImage,SliderConfig,
    Footer,FooterLink,GrouLinkFooter,License
)

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


class LicenseSerializer (serializers.ModelSerializer) : 

    class Meta : 
        model = License
        exclude = ["id","footer"]

class FooterLinkSerializer (serializers.ModelSerializer) : 

    class Meta : 
        model = FooterLink
        exclude = ["id","group_link"]

class GrouLinkFooterSerializer (serializers.ModelSerializer) : 

    links = FooterLinkSerializer(many=True)

    class Meta : 
        model = GrouLinkFooter
        exclude = ["id","footer"]

class FooterSerializer (serializers.ModelSerializer) :

    licenses = LicenseSerializer(many=True) 

    group_links = GrouLinkFooterSerializer(many=True)
    
    class Meta : 
        model = Footer
        exclude = ["id","is_active"]


class IndexSerializer (serializers.Serializer) : 

    car_brands = BrandSerializer(many=True)

    brand_countries = CountrySerializer(many=True)

    yadak_sadra_brands = BrandSerializer(many=True)

    slider = SliderConfigSerializer()




