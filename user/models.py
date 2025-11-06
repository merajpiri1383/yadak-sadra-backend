import uuid
import hashlib
import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.core.validators import MinLengthValidator,MaxLengthValidator
from user.manager import UserManager



class User (AbstractBaseUser,PermissionsMixin) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    username = models.CharField(max_length=300,unique=True)

    phone = models.SlugField(
        max_length=11,
        validators=[
            MinLengthValidator(11),
            MaxLengthValidator(11),
        ],
        unique=True,
        )
    
    opt_code_hashed = models.CharField(null=True,blank=True,max_length=256)
    
    is_active = models.BooleanField(default=False,)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["phone"]

    def __str__ (self) : 
        return f"{self.username} -- {self.phone}"
    
    def change_otp_code (self,code) : 
        random_code = str(code).encode("utf-8")
        hashed_random_code = hashlib.sha256(random_code)
        self.opt_code_hashed = hashed_random_code.hexdigest()
        self.save()
