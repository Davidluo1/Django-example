from rest_framework import serializers

class UpdateCartRequest(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1, max_value=10)