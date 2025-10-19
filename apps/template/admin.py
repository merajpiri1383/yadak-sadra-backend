from django.contrib import admin
from apps.template.models import SlideBox,SlideImage,SliderConfig

class SlideImageInline (admin.TabularInline) : 
    extra = 0
    exclude = ["id"]
    model = SlideImage


class SlideBoxInline (admin.TabularInline) : 
    extra = 0
    exclude = ['id']
    model = SlideBox

@admin.register(SliderConfig)
class SliderConfigAdmin (admin.ModelAdmin) :
    exclude = ["id"]
    inlines = [SlideImageInline,SlideBoxInline]