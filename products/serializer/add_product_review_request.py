from rest_framework import serializers

class AddProductReviewRequest(serializers.Serializer):
    rating = serializers.FloatField(min_value=1, max_value=5)
    comment = serializers.CharField(max_length = 1000)