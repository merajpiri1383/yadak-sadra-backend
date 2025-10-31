import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from user.models import User


phone_regex = re.compile("09[0-9]{9}")
password_regex = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*[1-9]).{8,16}$")


class RegisterSerializer (serializers.ModelSerializer) : 

    password = serializers.SlugField(required=True)

    class Meta : 
        model = User
        fields = ["username","phone","password"]

    def validate(self,attrs) : 
        if "phone" in attrs and not phone_regex.findall(attrs["phone"]) : 
            raise ValidationError({"phone" : "enter valid number ."})
        if "password" in attrs and not password_regex.match(attrs["password"]) : 
            raise ValidationError(
                {"password" : "password must contains Uppercase , lowercase, number "
                "and at least have 8 chatacter"})
        return super().validate(attrs)
    


class UserSerializer (serializers.ModelSerializer) : 

    class Meta : 
        model = User
        fields = ["username","phone"]

