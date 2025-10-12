from django.urls import path
from apps.product import api

urlpatterns = [
    path("all/",api.ProductsAPIView.as_view(),name="products")
]