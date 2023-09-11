from rest_framework import serializers
from ..models import AtendanceTime

class AtendanceTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AtendanceTime
        fields = ('id', 'created_at', 'day', 'hour')
        read_only_fields = ('id', 'created_at')