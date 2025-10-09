import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from user.manager import UserManager
from django.core.validators import MinLengthValidator,MaxLengthValidator


class User (AbstractBaseUser,PermissionsMixin) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    username = models.CharField(max_length=300,unique=True)

    phone = models.SlugField(
        max_length=11,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(11),
        ]
        )
    
    opt_code = models.SlugField(
        validators=[
            MinLengthValidator(4),
            MaxLengthValidator(6)
        ]
    )
    
    is_active = models.BooleanField(default=False,)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["phone"]

    def __str__ (self) : 
        return f"{self.username} -- {self.phone}"