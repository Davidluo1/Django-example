from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User, UserOtp
from user.serializer.user_signup_request import SignUpRequest
from user.serializer.user_table_request import UserSerializer
import random
from django.db import transaction

class UserSignUpView(APIView):
    """User SignUp View class"""
    @transaction.atomic
    def post(self,request):
        req_data = request.data
        request_data = SignUpRequest(data=req_data)
        # _ when not sure what input 
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        
        # resolve duplicate email/phone number by returning an error response
        if User.objects.filter(email = req_data["email"]).exists():
            return Response({"msg" : "Email already exists"}, status=400)
        if User.objects.filter(contact_number = req_data["contact_number"]).exists():
            return Response({"msg" : "Phone already being signed up to other user account"}, status=400)
        # create an user table element with password encrypted
        user_instance = UserSerializer.create(req_data)
        # create an random otp value for the user
        UserOtp.objects.create(otp_value = random.randint(100000, 999999), user= user_instance)
        return Response({"msg" : "Sign up successful!!!"}, status=200)
        