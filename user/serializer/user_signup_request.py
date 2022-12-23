from rest_framework import serializers

class SignUpRequest(serializers.Serializer):
    """Sign up request elements"""
    
    password = serializers.CharField(max_length = 50)
    email = serializers.CharField(max_length = 50)
    first_name = serializers.CharField(max_length = 50)
    contact_number = serializers.IntegerField()
    username = serializers.CharField(max_length = 50)
    