from django.db import models

class AtendanceTime(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    day = models.DateField()
    hour = models.TimeField()