from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
import boto3
from datetime import datetime
from django.conf import settings
from player.models import Player

class AddPlayerImage(APIView):
    """Add player image for player"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, country_id, player_id):
        user = request.user
        request_file = request.FILES.get("image", None)
        # player_qs = Player.objects.filter(country_id=country_id, id=player_id)
        # if player_qs[0].image:
        #     request_file = player_qs[0].image
        now= datetime.now()
        time = now.strftime("%H:%M:%S")
        time = time.replace(":", "")
        image_file_check = ['png','jpg','gif','svg']
        file_name = time + "/" + request_file.name
        if file_name.split('.')[-1].lower() not in image_file_check:
            return Response({"msg" : "Incorrect image file format."})
        if request_file:
            if Player.objects.filter(country_id=country_id, id=player_id).exists():
                s3 = boto3.resource('s3', aws_access_key_id = settings.PLAYER_AWS_ACCESS_KEY_ID,
                    aws_secret_access_key= settings.PLAYER_AWS_SECRET_ACCESS_KEY,
                    endpoint_url = settings.PLAYER_ENDPOINT_URL)
                bucket = s3.Bucket(settings.PLAYER_BUCKET_NAME)
                bucket.put_object(Key=file_name, Body=request_file)

                file_url = settings.PLAYER_FILE_URL + file_name
                Player.objects.filter(country_id=country_id, id=player_id).update(image = file_url)
                return Response({"msg" : "Image updated"}, status = 200)
            else:
                return Response({"msg" : "Invalid product"}, status = 400)
        else:
            return Response({"msg" : "File not found"}, status = 400) 
        
        
        
