from rest_framework import serializers

class CountryRequest(serializers.Serializer):
    "Country serializer"
    name = serializers.CharField(max_length=100)
    flag = serializers.CharField(max_length=500)
    continent = serializers.CharField(max_length=100)
    
    