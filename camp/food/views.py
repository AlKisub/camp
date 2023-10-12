from django.shortcuts import render
from django.http import HttpResponse
from .models import Food

def index(request):
    inventory = Food.objects.all()
    if not inventory:
        inventory = []
    return render(request, 'food/events_list.html', {'events_list': inventory})
# Create your views here.
