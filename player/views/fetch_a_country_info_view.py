from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import boto3
from datetime import datetime
from django.conf import settings
from player.models import Country


class GetCountry(APIView):
    """Get certain Countries"""
    permission_classes = [(IsAuthenticated)]
    
    def get(self, request, country_id):
        """get certain country info from the database that is active"""
        user = request.user
        country_qs = Country.objects.filter(id=country_id, is_deleted=False)
        if country_qs.exists():
            resp=[]
            for data in country_qs:
                resp.append({"name":data.name, "cotinent":data.continent})
            return Response({"Data" : resp}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country added"}, status=400) 
