from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from user.models import Address


class AddressDefaultView(APIView):
    """User Info View class"""
    
     # Identify whether the user is authenticated or not
    permission_classes = [(IsAuthenticated)]
    
    @transaction.atomic
    def put(self,request, address_id):
        user = request.user
        if Address.objects.filter(user=user, id=address_id).exists():
            Address.objects.filter(id=address_id).update(is_default=True)
            return Response({"msg" : "Address success"}, status=200)
        return Response({"msg" : "Address failed"}, status=400)
        