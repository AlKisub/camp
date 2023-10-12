from django.shortcuts import render
from django.http import HttpResponse
from .models import Retailer

def index(request):
    inventory = Retailer.objects.all()
    if not inventory:
        inventory = []
    return render(request, 'retailer/events_list.html', {'events_list': inventory})
# Create your views here.
