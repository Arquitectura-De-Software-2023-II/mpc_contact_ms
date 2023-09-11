from django.db import models
from .doctor_model import Doctor

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    
    class Meta:
        app_label = 'service_info_ms'