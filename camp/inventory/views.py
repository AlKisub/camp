from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory

def index(request):
    inventory = Inventory.objects.all()
    if not inventory:
        inventory = []
    return render(request, 'inventory/events_list.html', {'events_list': inventory})
# Create your views here.
