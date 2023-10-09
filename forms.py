# dashboard_app/forms.py
from django import forms
from .models import DashboardData

class DashboardDataForm(forms.ModelForm):
    class Meta:
        model = DashboardData
        fields = '__all__'
