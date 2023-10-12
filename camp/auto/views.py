from django.shortcuts import render
from django.http import HttpResponse
from .models import Auto

def index(request):
    inventory = Auto.objects.all()
    if not inventory:
        inventory = []
    return render(request, 'auto/events_list.html', {'events_list': inventory})
# Create your views here.
