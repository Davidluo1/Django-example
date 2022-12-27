from rest_framework import serializers

class CategoryRequest(serializers.Serializer):
    category_name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    logo = serializers.CharField(max_length=100)