from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
import boto3
from datetime import datetime
from django.conf import settings
from player.models import Country

class AddCountryImage(APIView):
    """Add country image"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, country_id):
        user = request.user
        # fetch flag image file from request
        request_file = request.FILES.get("flag", None)
        # get current time
        now= datetime.now()
        time = now.strftime("%H:%M:%S")
        time = time.replace(":", "")
        # image file check
        flag_file_check = ['png','jpg','gif', 'svg']
        file_name = time + "/" + request_file.name
        if file_name.split('.')[-1].lower() not in flag_file_check:
            return Response({"msg" : "Incorrect image file format."})
        if request_file:
            if Country.objects.filter(id = country_id).exists():
                s3 = boto3.resource('s3', aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key= settings.AWS_SECRET_ACCESS_KEY,
                    endpoint_url = settings.ENDPOINT_URL)
                bucket = s3.Bucket(settings.BUCKET_NAME)
                bucket.put_object(Key=file_name, Body = request_file)

                file_url = settings.FILE_URL + file_name
                Country.objects.filter(id = country_id).update(flag = file_url)
                return Response({"msg" : "Flag updated"}, status = 200)
            else:
                return Response({"msg" : "Invalid product"}, status = 400)
        else:
            return Response({"msg" : "File not found"}, status = 400) 
        
        
        
