from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from player.serializer import MatchRequest
from player.models import Match, Player
from utils.file_data_check import MatchInDatabaseValidCheck


class AddMatchPlayer(APIView):
    """Add match player"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request, match_id, match_teams_id):
        """Add a player to the match"""
        user = request.user
        req_data = request.data
        request_data = MatchRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        # Find the match if it is not deleted and exist in database
        # if MatchInDatabaseValidCheck(match_id):
        if Match.objects.filter(id=match_id, is_deleted=False):
            match_team_qs = Player.objects.filter(country_id=match_teams_id, is_deleted=False)
            # check is the plyer data already eixst in the team
            if match_team_qs.filter(data=req_data).exists():
                return Response({"msg" : "Player already in the team"})
            # limit team up to 20 players
            if match_team_qs.all().count() > 20:
                return Response({"msg" : "Team is limited to 20 players"})
            # Add player to the team
            match_team_qs.create(data=req_data, country_id=match_teams_id)
            
        return Response({"msg" : "Player added to match"}, status=status.HTTP_200_OK) 
        
    
