from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import boto3
from datetime import datetime
from django.conf import settings
from player.models import Player


class GetPlayer(APIView):
    """Get certain Player"""
    permission_classes = [(IsAuthenticated)]
    
    def get(self, request, country_id, player_id):
        """get certain Player info from the database that is active"""
        user = request.user
        player_qs = Player.objects.filter(country_id=country_id, id=player_id, is_deleted=False)
        if player_qs.exists():
            resp=[]
            for player in player_qs:
                resp.append({"id":player.id, "name":player.name, "dob":player.dob,
                             "status":player.status, "height":player.height, "weight":player.weight})
            return Response({"Data" : resp}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country added"}, status=400) 
