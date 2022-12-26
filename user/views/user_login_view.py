from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from user.serializer.user_login_request import LoginRequest
import random
from rest_framework.authtoken.models import Token

class UserLoginView(APIView):
    """User SignUp View class"""
    
    def post(self,request):
        req_data = request.data
        request_data = LoginRequest(data=req_data)
        # _ when not sure what input 
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        email = req_data['email']
        # see if user email exist
        qs = User.objects.filter(email=email)
        if qs.exists():
            password = req_data['password']
            user_instance = qs[0]
            if user_instance.otp_verify:
                password = req_data['password']
                # bool password check
                if user_instance.check_password(password):
                    # create a token key for the user once logged in
                    token, created = Token.objects.get_or_create(user=user_instance)
                    #print(token)
                    return Response({"msg" : "login up successful!!!"}, status=200)
                return Response({"msg" : "Incorrect password"}, status=400)
            return Response({"msg" : "Account not activated"}, status=400)
        return Response({"msg" : "Account does not exist"}, status=400)
        