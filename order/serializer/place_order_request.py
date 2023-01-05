from rest_framework import serializers

class PlaceOrderRequest(serializers.Serializer):
    shipping_address = serializers.CharField(max_length=1000)
    billing_address = serializers.CharField(max_length=1000)