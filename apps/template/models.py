from django.db import models
import uuid


class SliderConfig (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    is_active = models.BooleanField(default=False)

    def __str__ (self) : 
        return "Slider Config"
    

class SlideBox (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    slider = models.ForeignKey(
        to=SliderConfig,
        on_delete=models.CASCADE,
        related_name="boxes",
    )

    image_url = models.ImageField(upload_to="media/template/slider/slide-box")

    title =  models.CharField(max_length=256)

    link = models.CharField(default="/",max_length=256)

    def __str__ (self) : 
        return str(self.title)

class SlideImage (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    slider = models.ForeignKey(
        to=SliderConfig,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image_url = models.ImageField(upload_to="media/template/slider/slides")

    def __str__ (self) : 
        return str(self.image_url)


class Footer (models.Model) : 
    
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    is_active = models.BooleanField(default=False)

    instagram_page = models.CharField(max_length=128,null=True,blank=True)

    telegram_channel = models.CharField(max_length=128,null=True,blank=True)

    whatsapp_support = models.CharField(max_length=128,null=True,blank=True)

    phone = models.CharField(max_length=13,null=True,blank=True)

    email = models.EmailField(null=True,blank=True)

    address = models.CharField(max_length=256,null=True,blank=True)

    description = models.TextField(null=True,blank=True)

    def __str__ (self) : 
        return "Footer"
    

class License (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)

    footer = models.ForeignKey(
        to=Footer,
        on_delete=models.CASCADE,
        related_name="licenses",
    )

    image = models.ImageField(upload_to="template/footer/license/")

    url = models.CharField(max_length=256)

    def __str__ (self) : 
        return str(self.url)


class GrouLinkFooter (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    footer = models.ForeignKey(
        to=Footer,
        on_delete=models.CASCADE,
        related_name="group_links",
    )

    title = models.CharField(max_length=128)

    def __str__ (self) : 
        return str(self.title)
    

class FooterLink (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    group_link = models.ForeignKey(
        to=GrouLinkFooter,
        on_delete=models.CASCADE,
        related_name="links",
    )

    title = models.CharField(max_length=64)

    url = models.CharField(max_length=256,)

    def __str__ (self) : 
        return str(self.title)

