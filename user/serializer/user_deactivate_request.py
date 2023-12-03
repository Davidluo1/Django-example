from rest_framework import serializers

class UserDeactivateRequest(serializers.Serializer):
    """"User deactivate input class"""
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    otp = serializers.CharField(max_length=50)
    
