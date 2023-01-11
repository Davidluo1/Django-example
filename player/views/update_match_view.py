from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from player.serializer import MatchRequest
from player.models import Match
from utils.file_data_check import MatchInDatabaseValidCheck

class UpdateMatch(APIView):
    """Update match"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, match_id):
        """Modify a Match"""
        user = request.user
        req_data = request.data
        request_data = MatchRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        # check for duplicate match
        match_qs = Match.objects.filter(id=match_id, venue=req_data['venue'], match_date=req_data['match_date'], 
                                        is_deleted=False)
        if match_qs.exists():
            match_qs.update()
            return Response({"msg" : "Match updated"}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Match not exist"}, status=400)
        
        
        
    @transaction.atomic
    def delete(self, request, match_id):
        """Delete a Match"""
        user = request.user
        # check is match exist and not deleted
        # match_qs=MatchInDatabaseValidCheck(match_id)
        match_qs = Match.objects.filter(id=match_id, is_deleted=False)
        if match_qs.exists():
            match_qs.delete()
            #match_qs.update(is_deleted=True)
            return Response({"msg" : "Match deleted"}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Match not exist"}, status=400) 
