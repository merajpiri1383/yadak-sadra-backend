from django.db import models
import uuid
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator


class Country (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    name = models.CharField(max_length=256,unique=True)

    slug = models.SlugField(allow_unicode=True,null=True,blank=True)

    flag = models.ImageField(upload_to="product/country/",null=True,blank=True)

    def __str__ (self) : 
        return str(self.name)
    

    def get_most_brands (self,count=5) : 
        return Country.objects.annotate(
            country_brands=models.Count("brand")
        ).order_by("-country_brands")[:count]
    

    def save(self,**kwarges) : 
        self.slug = slugify(self.name,allow_unicode=True)
        return super().save(**kwarges)


class Brand (models.Model) : 
    
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    is_own = models.BooleanField(default=False,verbose_name="is brand is for this company ?")

    country = models.ForeignKey(
        to=Country,
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
    


class Product (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    title = models.CharField(max_length=256)

    slug = models.SlugField(allow_unicode=True,null=True,blank=True)

    technical_code = models.CharField(max_length=256,null=True,blank=True)

    commercial_code = models.CharField(max_length=256,null=True,blank=True)

    main_image = models.ImageField(upload_to="product/images")

    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        related_name="products"
    )

    price = models.PositiveIntegerField()

    discount_percent = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0),MaxValueValidator(100)]
    )

    brand = models.ForeignKey(
        to=Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    short_description = models.TextField(null=True,blank=True)

    description = models.TextField(null=True,blank=True)

    time_added = models.DateTimeField(auto_now_add=True)

    is_available = models.BooleanField(default=True)

    def __str__ (self) : 
        return str(self.title)
    
    def save(self,**kwargs) : 
        self.slug = slugify(self.title,allow_unicode=True)
        return super().save(**kwargs)
    


class ProductImage (models.Model) :
    
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="product/images")

    def __str__ (self) : 
        return f"{self.product.title}"