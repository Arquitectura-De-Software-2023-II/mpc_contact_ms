from rest_framework import viewsets, permissions
from .models import AtendanceTime, Doctor, Review, Service
from .serializers import AtendanceTimeSerializer, DoctorSerializer, ReviewSerializer, ServiceSerializer

class AtendanceTimeViewSet(viewsets.ModelViewSet):
    queryset = AtendanceTime.objects.all()
    serializer_class = AtendanceTimeSerializer
    permission_classes = [permissions.AllowAny]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.AllowAny]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]
