from django.shortcuts import render

# Create your views here.

def admin_dashboard(request):
    context = {}
    return render(request, 'dashboard/index.html', context)