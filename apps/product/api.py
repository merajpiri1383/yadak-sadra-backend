from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductsAPIView (APIView) : 

    def get(self,request) : 
        params = request.GET

        products = Product.objects.all()

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
                context={'request' : request}
            ).data
        }
        return Response(data,status.HTTP_200_OK)