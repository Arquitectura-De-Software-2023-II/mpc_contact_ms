from rest_framework import serializers
from ..models import Service

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = ('id', 'created_at', 'name', 'description', 'price')
        read_only_fields = ('id', 'created_at')