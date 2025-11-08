from django.db import models
import uuid
from django.contrib.auth import get_user_model
from apps.product.models import Product



class Cart (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="carts",
    )

    is_open = models.BooleanField(default=True)

    is_paid = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)

    total_price = models.IntegerField(default=0)

    def __str__ (self) : 
        return f"Cart -- {self.user}"



class CartProduct (models.Model) : 

    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    cart = models.ForeignKey(
        to=Cart,
        on_delete=models.CASCADE,
        related_name="cart_products"
    )

    product = models.ForeignKey(
        to=Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    count = models.PositiveIntegerField(default=0)

    def __str__ (self) : 
        return f"Cart : {self.cart} | Product : {self.product.title} | Count : {self.count}"


