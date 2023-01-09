from rest_framework import serializers

class MatchRequest(serializers.Serializer):
    "Match serializer"
    match_date = serializers.CharField(max_length=100)
    venue = serializers.CharField(max_length=500)
    
    