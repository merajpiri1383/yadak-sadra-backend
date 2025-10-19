from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from apps.product.models import Brand,Country
from apps.product.serializers import (
    BrandSerializer,
    CountrySerializer
)
from apps.template.serializers import (
    IndexSerializer,
    SliderConfigSerializer
)
from apps.template.models import SliderConfig
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class IndexAPIView(APIView) : 


    @swagger_auto_schema(
        operation_summary="Index Page",
        responses={
            200 : openapi.Response("Ok",IndexSerializer())
        }
    )
    def get(self,request) : 

        data = {
            "car_brands" : BrandSerializer(
                Brand.objects.filter(is_own=False)[:8],
                many=True,
                context={"request":request}).data,
            "brand_countries" : CountrySerializer(
                Country().get_most_brands(),
                many=True,
                context={'request': request}
            ).data,
            "yadak_sadra_brands" : BrandSerializer(
                Brand.objects.filter(is_own=True)[:6],
                many=True,
                context={"request":request}).data,
            "slider" : SliderConfigSerializer(
                SliderConfig.objects.filter(is_active=True).last(),
                context={"request" : request}
            ).data,
        }
        return Response(data=data,status=status.HTTP_200_OK)