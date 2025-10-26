from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.product.models import ProductCategory,Brand,Country
from apps.product.serializers import (
    ProductSerializer,ProductCategoryResponseSerializer,
    BrandSerializer,CountrySerializer,
)
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Count
    



class ProductCategoryAPIView (APIView) : 

    @swagger_auto_schema(
        operation_summary="Get Product Base on Category",
        responses={
            "200" : ProductCategoryResponseSerializer(),
        }
    )
    def get(self,request,slug) : 

        params = request.GET

        try : 
            products = ProductCategory.objects.get(slug=slug).products.all()
        except : 
            return Response(
                data={"error" : "not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if "brand" in params.keys() and params["brand"].strip() != "" : 
            brand = params["brand"].strip()
            products = products.filter(brand__slug=brand)
        
        if "country" in params.keys() and params["country"].strip() != "" : 
            country = params["country"]
            products = products.filter(country__slug=country)
        
        if "order" in params.keys() : 
            order = params["order"]
            match order : 
                case "new" : 
                    products = products.order_by("-time_added")
                case "expense" : 
                    products = products.order_by("-price")
                case "cheep" : 
                    products = products.order_by("price")

        data = {
            "products" : ProductSerializer(
                products,
                many=True,
                context={"request" : request},
            ).data,
            "count" : products.count(),
            "brands" : BrandSerializer(
                Brand.objects.annotate(product_count=Count("products")).order_by("-product_count")[0:5],
                many=True,
                context={"request" : request},
            ).data,
            "countries" : CountrySerializer(
                Country.objects.annotate(product_count=Count("products")).order_by("-product_count")[0:5],
                many=True,
                context={'request' : request}
            ).data,
        }
        return Response(data,status.HTTP_200_OK)