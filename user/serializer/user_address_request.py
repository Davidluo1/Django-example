from rest_framework import serializers

class AddressRequest(serializers.Serializer):
    street_address = serializers.CharField(max_length = 245)
    state = serializers.CharField(max_length = 200)
    city = serializers.CharField(max_length = 200)
    pincode = serializers.IntegerField()
    nickname = serializers.CharField(max_length = 50, required=False)