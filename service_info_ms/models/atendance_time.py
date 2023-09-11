from django.db import models
from .doctor_model import Doctor

class AtendanceTime(models.Model):
    
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    day = models.DateField()
    hour = models.TimeField()

    class Meta:
        app_label = 'service_info_ms'