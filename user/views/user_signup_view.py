from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.serializer import SignUpRequest
import random

class UserSignUpView(APIView):
    """User SignUp View class"""
    
    def post(self, request):
        req_data = request.data
        request_data = SignUpRequest(data=req_data)
        # _ when not sure what input 
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        
        
        return Response({"msg" : "Sign up successful!!!"})
        