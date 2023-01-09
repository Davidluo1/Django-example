from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from player.serializer import PlayerRequest
from player.models import Player


class UpdatePlayer(APIView):
    """Update player"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, country_id, player_id):
        """Modify a player"""
        user = request.user
        req_data = request.data
        request_data = PlayerRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        player_qs = Player.objects.filter(country_id=country_id, id=player_id)
        if player_qs.exists():
            player_qs.update(id=country_id, name=req_data['name'], 
                                          dob=req_data['dob'], status=req_data['status'], 
                                          height=req_data['height'], weight=req_data['weight'])
            return Response({"msg" : "Player updated"}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Player not exist"}, status=400)
        
        
        
    @transaction.atomic
    def delete(self, request, country_id, player_id):
        """Delete a country"""
        user = request.user
        player_qs = Player.objects.filter(country_id=country_id, id=player_id, is_deleted=False)
        if player_qs.exists():
            player_qs.delete()
            #player_qs.update(is_deleted=True)
            return Response({"msg" : "Player deleted"}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Player not exist"}, status=400) 
