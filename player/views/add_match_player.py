from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from player.serializer import MatchRequest
from player.models import Match


class AddMatchPlayer(APIView):
    """Add Country"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request):
        """Add a player to the match"""
        user = request.user
        req_data = request.data
        request_data = MatchRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        
        return Response({"msg" : "Player added to match"}, status=status.HTTP_200_OK) 
        
    
    def get(self, request):
        """get match player list"""
        user = request.user
        match_qs = Match.objects.filter(is_deleted=False)
        total=0
        resp=[]
        if match_qs:
            for data in match_qs:
                total+=1
                resp.append({})
            return Response({"Total players in match" : total, "List" : resp}, status=status.HTTP_200_OK)
        return Response({"msg" : "Inavlid entry"}, status=400) 

