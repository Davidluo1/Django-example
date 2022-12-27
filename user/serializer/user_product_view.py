from rest_framework import serializers

class ProductRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    image = serializers.ImageField(upload_to='')