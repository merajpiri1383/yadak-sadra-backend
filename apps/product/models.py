from django.db import models
import uuid
from django.utils.text import slugify


class BrandCountry (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    name = models.CharField(max_length=256,unique=True)

    slug = models.SlugField(allow_unicode=True,null=True,blank=True)

    def __str__ (self) : 
        return str(self.name)
    

    def save(self,**kwarges) : 
        self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwarges)


class Brand (models.Model) : 
    
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    is_own = models.BooleanField(default=False,verbose_name="is brand is for this company ?")

    country = models.ForeignKey(
        to=BrandCountry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="the country brand belongs to "
    )

    logo = models.ImageField(upload_to="product/brand/")

    name = models.CharField(max_length=256)

    slug = models.SlugField(allow_unicode=True,null=True,blank=True)


    def __str__ (self) : 
        return str(self.name)
    
    def save(self,**kwargs) : 
        self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwargs)