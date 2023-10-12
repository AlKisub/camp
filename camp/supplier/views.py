from django.shortcuts import render
from django.http import HttpResponse
from .models import Supplier

def index(request):
    inventory = Supplier.objects.all()
    if not inventory:
        inventory = []
    return render(request, 'supplier/events_list.html', {'events_list': inventory})
# Create your views here.
