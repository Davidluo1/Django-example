from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from player.serializer import PlayerRequest
from player.models import Player

class AddPlayer(APIView):
    """Add player"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request, country_id):
        user = request.user
        req_data = request.data
        request_data = PlayerRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        if Player.objects.filter(country_id=country_id, name=req_data['name'], dob=req_data['dob'], 
                                          height=req_data['height'], weight=req_data['weight'], 
                                          image=req_data['image']).exists():
            return Response({"msg" : "Player already exist"}, status=400) 
        Player.objects.create(country_id=country_id, name=req_data['name'], 
                                          dob=req_data['dob'], status=req_data['status'], 
                                          height=req_data['height'], weight=req_data['weight'], 
                                          image=req_data['image'])
        return Response({"msg" : "Player added"}, status=status.HTTP_200_OK) 
        
        
         
    @transaction.atomic
    def get(self, request, country_id):
        """Get all player data"""
        user = request.user
        player_qs = Player.objects.filter(country_id=country_id, is_deleted=False)
        resp=[]
        total=0
        if player_qs:
            for player in player_qs:
                total+=1
                resp.append({"id":player.id, "name":player.name, "dob":player.dob,
                             "status":player.status, "height":player.height, "weight":player.weight})
            return Response({"Total players" : total, "Player list" : resp}, status=400) 
        return Response({"msg" : "Player added"}, status=status.HTTP_200_OK) 