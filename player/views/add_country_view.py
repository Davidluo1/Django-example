from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
import boto3
from datetime import datetime
from django.conf import settings
from player.serializer import CountryRequest
from player.models import Country


class AddCountry(APIView):
    """Add Country"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request):
        """Add a country to the database"""
        user = request.user
        req_data = request.data
        request_data = CountryRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        if Country.objects.filter(name=req_data['name'], flag=req_data['flag'], 
                                           continent=req_data['continent']).exists():
            return Response({"msg" : "Country already exist"}, status=400)
        Country.objects.create(name=req_data['name'], flag=req_data['flag'], 
                                           continent=req_data['continent'])
        request_file = request.FILES.get("flag", None)
        # now= datetime.now()
        # time = now.strftime("%H:%M:%S")
        # time = time.replace(":", "")
        # image_file_check = ['png','jpeg','gif']
        # if file_name.split('.')[-1].lower() not in image_file_check:
        #     return Response({"msg" : "Incorrect image file format."})
        # file_name = time + "/" + request_file.name
        # if request_file:
        #     if Country.objects.filter(id = product_id).exists():
        #         s3 = boto3.resource('s3', aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
        #             aws_secret_access_key= settings.AWS_SECRET_ACCESS_KEY,
        #             endpoint_url = settings.ENDPOINT_URL)
        #         bucket = s3.Bucket(settings.BUCKET_NAME)
        #         bucket.put_object(Key=file_name, Body = request_file)

        #         file_url = settings.FILE_URL + file_name
        #         Player.objects.filter(id = product_id).update(image = file_url)
        #         return Response({"msg" : "Image updated"}, status = 200)
        #     else:
        #         return Response({"msg" : "Invalid product"}, status = 400) 
        return Response({"msg" : "Country added"}, status=status.HTTP_200_OK) 
        
    
    def get(self, request):
        """get all country info from the database that are active"""
        user = request.user
        country_qs = Country.objects.filter(is_deleted=False)
        total=0
        resp=[]
        if country_qs:
            for data in country_qs:
                total+=1
                resp.append({"id":data.id, "name":data.name, "continent":data.continent})
            return Response({"Total countries" : total, "List" : resp}, status=status.HTTP_200_OK)
        return Response({"msg" : "Empty"}, status=400) 

