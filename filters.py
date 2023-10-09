# dashboard_app/filters.py
import django_filters
from .models import DashboardData

class DashboardDataFilter(django_filters.FilterSet):
    class Meta:
        model = DashboardData
        fields = {
            'year': ['exact'],
            'country': ['exact'],
            'topics': ['exact'],
            'region': ['exact'],
        }
