from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
import boto3
from datetime import datetime
from django.conf import settings


class AddMatch(APIView):
    """Add match"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request):
        
        return Response({"msg" : "Player added"}, status=status.HTTP_200_OK) 
        
        
         
    @transaction.atomic
    def get(self, request):
        """Get all match data"""
        
        return Response({"msg" : "Player added"}, status=status.HTTP_200_OK) 