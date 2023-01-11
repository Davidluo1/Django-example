from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from player.models import Country
from utils.file_data_check import CountryInDatabaseValidCheck


class GetCountry(APIView):
    """Get certain Countries"""
    permission_classes = [(IsAuthenticated)]
    
    def get(self, request, country_id):
        """get certain country info from the database that is active"""
        user = request.user
        # filter a country in database and is not deleted
        # country_qs = CountryInDatabaseValidCheck(country_id)
        country_qs = Country.objects.filter(id=country_id, is_deleted=False)
        if country_qs.exists():
            resp=[]
            resp.append({"name":country_qs[0].name, "cotinent":country_qs[0].continent})
            return Response({"Data" : resp}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country not exist or deleted"}, status=400) 
