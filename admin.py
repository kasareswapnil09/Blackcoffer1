# dashboard_app/admin.py
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import DashboardData

class DashboardDataResource(resources.ModelResource):
    class Meta:
        model = DashboardData

class DashboardDataAdmin(ImportExportModelAdmin):
    resource_class = DashboardDataResource

admin.site.register(DashboardData, DashboardDataAdmin)
