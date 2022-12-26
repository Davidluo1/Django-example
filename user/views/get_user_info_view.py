from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from rest_framework.permissions import IsAuthenticated

class UserInfo(APIView):
    """User Info View class"""
    
     # Identify whether the user is authenticated or not
    permission_classes = [(IsAuthenticated)]
    
    def get(self,request):
        user_data = request.data
        email = user_data['email']
        contact = user_data['contact_number']
        # find match email
        qs = User.objects.filter(email=email, contact_number = contact)
        if qs:
            user_instance = qs[0]
            return Response({"first_name" : user_instance.first_name, "contact" : 
                user_instance.contact_number, "username" : user_instance.username})
        return Response({"msg" : "User not found"}, status=400)
        