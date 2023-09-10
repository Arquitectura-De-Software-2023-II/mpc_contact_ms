from django.db import models

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    rate = models.FloatField()
    