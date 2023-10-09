# dashboard_app/models.py
from django.db import models

class DashboardData(models.Model):
    intensity = models.CharField(max_length=255)
    likelihood = models.CharField(max_length=255)
    relevance = models.CharField(max_length=255)
    year = models.CharField(max_length=4) 
    country = models.CharField(max_length=255)
    topics = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

