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
