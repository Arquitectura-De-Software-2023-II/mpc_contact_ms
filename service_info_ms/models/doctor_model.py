from django.db import models

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    rating = models.FloatField()
