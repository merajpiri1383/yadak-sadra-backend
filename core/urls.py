from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema = get_schema_view(
    info=openapi.Info(
        title="Yadak-Sadra",
        default_version="1.0.0",
        license=openapi.License(name="MIT")
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",schema.with_ui("swagger",cache_timeout=0),name="swagger")
]
