from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
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
            resp.append({"id":player_qs[0].id, "name":player_qs[0].name, "dob":player_qs[0].dob,
                             "status":player_qs[0].status, "height":player_qs[0].height, "weight":player_qs[0].weight})
            return Response({"Data" : resp}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country added"}, status=400) 
