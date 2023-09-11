from rest_framework import serializers
from ..models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = ('id', 'created_at', 'name', 'title', 'rating', 'address', 'phone', 'email', 'image', 'rating')
        read_only_fields = ('id', 'created_at')