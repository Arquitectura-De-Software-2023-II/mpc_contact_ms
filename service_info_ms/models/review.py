from django.db import models
from .doctor_model import Doctor

class Review(models.Model):

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    description = models.CharField(max_length=500)
    rate = models.FloatField()

    class Meta:
        app_label = 'service_info_ms'
    