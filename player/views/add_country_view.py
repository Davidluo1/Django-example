from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from player.serializer import CountryRequest
from player.models import Country


class AddCountry(APIView):
    """Add Country"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def post(self, request):
        """Add a country to the database"""
        user = request.user
        req_data = request.data
        request_data = CountryRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        # check is the country already in the database
        if Country.objects.filter(name=req_data['name'], flag=req_data['flag'], 
                                           continent=req_data['continent']).exists():
            return Response({"msg" : "Country already exist"}, status=400)
        # create the country into database
        Country.objects.create(name=req_data['name'], flag=req_data['flag'], 
                                           continent=req_data['continent'])

        return Response({"msg" : "Country added"}, status=status.HTTP_200_OK) 
        
    
    def get(self, request):
        """get all country info from the database that are active"""
        user = request.user
        # filter country that is not deleted in the database
        country_qs = Country.objects.filter(is_deleted=False)
        # total number of countries
        total=0
        # countries data
        resp=[]
        if country_qs:
            for data in country_qs:
                total+=1
                resp.append({"id":data.id, "name":data.name, "continent":data.continent})
            return Response({"Total countries" : total, "List" : resp}, status=status.HTTP_200_OK)
        return Response({"msg" : "Empty"}, status=400) 

