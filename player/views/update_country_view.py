from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from player.serializer import CountryRequest
from player.models import Country


class UpdateCountry(APIView):
    """Update country"""
    permission_classes = [(IsAuthenticated)]

    @transaction.atomic
    def put(self, request, country_id):
        """Modify a country"""
        user = request.user
        req_data = request.data
        request_data = CountryRequest(data = req_data)
        _ = request_data.is_valid(raise_exception = True)
        req_data = request_data.validated_data
        country_qs = Country.objects.filter(id=country_id, is_deleted=False)
        if country_qs.exists():
            country_qs.update(id=country_id, name=req_data['name'], flag=req_data['flag'], 
                                           continent=req_data['continent'])
            return Response({"msg" : "Country updated"}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country not exist"}, status=400)
        
        
        
    @transaction.atomic
    def delete(self, request, country_id):
        """Delete a country"""
        user = request.user
        country_qs = Country.objects.filter(id=country_id, is_deleted=False)
        if country_qs.exists():
            country_qs.delete()
            #country_qs.update(is_deleted=True)
            return Response({"msg" : "Country deleted"}, status=status.HTTP_200_OK) 
        return Response({"msg" : "Country not exist"}, status=400) 
