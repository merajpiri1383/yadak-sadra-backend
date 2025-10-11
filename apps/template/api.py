from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from apps.product.models import Brand
from apps.product.serializers import BrandSerializer



class IndexAPIView(APIView) : 

    def get(self,request) : 

        data = {
            "car_brands" : BrandSerializer(
                Brand.objects.all()[:10],
                many=True,
                context={"request":request}).data,
        }
        return Response(data=data,status=status.HTTP_200_OK)