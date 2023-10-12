from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    inventory = Product.objects.all()
    if not inventory:
        inventory = []
    return render(request, 'product/events_list.html', {'events_list': inventory})
# Create your views here.
