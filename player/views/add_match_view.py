from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from datetime import datetime
from player.models import Player, Match
from player.serializer.match_request import MatchRequest
from django.core.paginator import Paginator

class AddMatch(APIView):
    """Add match"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request, country_id_one, country_id_two):
        user = request.user
        req_data = request.data
        request_data = MatchRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        team_white = Player.objects.filter(country_id=country_id_one)
        team_black = Player.objects.filter(country_id=country_id_two)
        now= datetime.now()
        time = now.strftime("%H:%M:%S")
        time = time.replace(":", "")
        if Match.objects.filter(match_date=time,venue=req_data['venue']).exists():
            return Response({"msg" : "Player added"}, status=400) 
        Match.objects.create(match_date=time,venue=req_data['venue'])
        return Response({"msg" : "Player added"}, status=status.HTTP_200_OK) 
        
        
         
    @transaction.atomic
    def get(self, request, country_id_one, country_id_two):
        """Get all match data"""
        venue_search = request.GET.get('venue', None)
        team_search = request.GET.get('team', None)
        date_search = request.GET.get('date', None)
        # find the category object that is not deleted in the database
        match_qs = Match.objects.filter(is_deleted = False)
        if venue_search:
            match_qs = Match.objects.filter(venue=venue_search)
        if team_search:
            match_qs = Match.objects.filter(venue=team_search)
        if date_search:
            match_qs = Match.objects.filter(venue=date_search)
        # user input page number, default as page 1
        page = request.GET.get("p", 1)
        # user input total size of the category, default as 10
        page_size = request.GET.get("psz", 10)
        # actual data of paginated form 
        paginator_object = Paginator(match_qs, page_size)
        # get total context of data, count, total_page_number
        object_list = paginator_object.page(page) 
        # actual data of paginated form 
        # import pdb; pdb.set_trace()
        page_info = {"total_matches" : paginator_object.count, "total_pages" : paginator_object.num_pages, "cur_page" : page}
        # has_next check next avaliable
        if object_list.has_next():
            page_info["next"] = object_list.next_page_number()
        else:
            page_info["next"] = None
        # has_previous check previous avaliable
        if object_list.has_previous():
            page_info["previous"] = object_list.previous_page_number()
        else:
            page_info["previous"] = None
        return Response({"msg" : "Player added"}, status=status.HTTP_200_OK) 