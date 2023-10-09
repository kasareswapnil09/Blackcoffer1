# dashboard_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import DashboardData
from .filters import DashboardDataFilter

def dashboard(request):
    data_list = DashboardData.objects.all()
    data_filter = DashboardDataFilter(request.GET, queryset=data_list)

    return render(request, 'dashboard.html', {'data': data_filter})



def update_data(request, data_id):
    instance = get_object_or_404(DashboardData, id=data_id)
    form = DashboardDataForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'update.html', {'form': form, 'instance': instance})