from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.crypto import constant_time_compare
from django.contrib.auth import get_user_model
import random
import hashlib
from rest_framework_simplejwt.tokens import RefreshToken
from apps.authentication.serializers import RegisterSerializer,UserSerializer
from apps.authentication.tasks import send_otp,check_user_is_active



class RegisterAPIView (APIView) : 

    def post (self,request) : 
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid() : 
            user = serializer.save()
            send_otp.apply_async(
                args=[user.id],
                link=check_user_is_active.si(user.id)
            )
            return Response({"data" : "otp has been sent"})
        else : 
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        


class ActivateUserAPIView (APIView) : 

    def post (self,request) : 
        try : 
            phone = request.data["phone"]
        except : 
            return Response({"phone" : "required ."},status.HTTP_400_BAD_REQUEST)

        try : 
            otp_code = request.data["otp_code"]
        except : 
            return Response({"otp_code" : "required ."},status.HTTP_400_BAD_REQUEST)
        
        # get user 
        try : 
            user = get_user_model().objects.get(phone=phone)
        except get_user_model().DoesNotExist : 
            return Response({"error" : "user does not exist ."})
        
        # change otp code to hashed
        hashed_otp = hashlib.sha256(str(otp_code).encode("utf-8"))
        if constant_time_compare(hashed_otp.hexdigest(),user.opt_code_hashed) : 
            user.is_active = True
            user.change_otp_code(random.randint(9999,99999))
            refresh_token = RefreshToken().for_user(user)
            data = {
                "access_token" : str(refresh_token.access_token),
                "refresh_token" : str(refresh_token),
                "user" : UserSerializer(user).data,
            }
            return Response(data,status.HTTP_200_OK)
        else : 
            return Response({"error" : "invalid otp_code ."},status.HTTP_200_OK)
        


    

