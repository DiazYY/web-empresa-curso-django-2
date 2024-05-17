from django.shortcuts import render
from .models import service

# Create your views here.
def services(request):
    services = service.objects.all()
    return render(request,'Services/services.html', {'services':services})
