from rest_framework import serializers
from ..models import Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id', 'created_at', 'description', 'rate')
        read_only_fields = ('id', 'created_at')