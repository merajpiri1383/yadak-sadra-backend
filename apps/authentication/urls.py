from django.urls import path
from apps.authentication import api


urlpatterns = [
    path("register/",api.RegisterAPIView.as_view(),name="register"),

    path("activate/",api.ActivateUserAPIView.as_view(),name="activate"),
]