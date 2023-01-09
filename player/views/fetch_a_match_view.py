from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from player.models import Match


class GetMatch(APIView):
    """Get certain match"""
    permission_classes = [(IsAuthenticated)]
    
    def get(self, request, match_id):
        """get certain country info from the database that is active"""
        user = request.user
        match_qs = Match.objects.filter(id=match_id, is_deleted=False)
        team_one = ""
        team_two = ""
        if match_qs.exists():
            resp=[]
            for data in match_qs:
                resp.append({"date":data.match_date, "venue":data.venue, "team one":team_one, 
                             "team two":team_two})
            return Response({"Data" : resp}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country added"}, status=400) 
