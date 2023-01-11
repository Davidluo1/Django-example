from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from player.models import Match, Country
from utils.file_data_check import MatchInDatabaseValidCheck

class GetMatch(APIView):
    """Get certain match"""
    permission_classes = [(IsAuthenticated)]
    
    def get(self, request, match_id):
        """get certain country info from the database that is active"""
        user = request.user
        # check is the match exist and not deleted
        # match_qs = MatchInDatabaseValidCheck(match_id)
        match_qs = Match.objects.filter(id=match_id, is_deleted=False)
        # find the country each team represents
        team_one = Country.objects.filter(id=match_qs[0].team_one_id)
        team_two = Country.objects.filter(id=match_qs[0].team_two_id)
        if match_qs.exists():
            resp=[]
            resp.append({"date":match_qs[0].match_date, "venue":match_qs[0].venue, "team one":team_one, 
                             "team two":team_two})
            return Response({"Data" : resp}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country added"}, status=400) 
