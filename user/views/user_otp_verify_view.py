from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User, UserOtp
from user.serializer.user_verify_request import OtpVerifyRequest
from django.db import transaction


class User_OtpVerifyView(APIView):
    """Opt verify for user"""
    @transaction.atomic
    def post(self,request):
        req_data = request.data
        request_data = OtpVerifyRequest(data=req_data)
        # _ when not sure what input 
        _ = request_data.is_valid(raise_exception=True)
        req_data = request_data.validated_data
        otp = req_data['otp']
        email = req_data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            user_instance = user_qs[0]
            otp_instance = UserOtp.objects.filter(user=user_instance, otp_value = otp)
            if otp_instance.exists():
                user_qs.update(otp_verify=True)
                return Response({"msg" : "OTP verified successfully"}, status = 200)
            return Response({"msg" : "Otp not correct"}, status=400)
        return Response({"msg" : "Account not exists"}, status=400)