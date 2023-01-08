from rest_framework import serializers

class PlayerRequest(serializers.Serializer):
    "Player serializer"
    name = serializers.CharField(max_length=100)
    dob = serializers.DateField()
    image = serializers.CharField()
    status = serializers.CharField(max_length=100)
    height = serializers.FloatField()
    weight = serializers.IntegerField()
    
