from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Events, Inventary_event, Product_event, Auto_event

def index(request):
    inventory = Events.objects.all()
    if not inventory:
        inventory = []
    return render(request, 'events/events_list.html', {'events_list': inventory})


def event(request, event_id):
    events = Events.objects.filter(pk=event_id)
    if not events:
        events = []
    inventory = Inventary_event.objects.filter(events=event_id)
    products = Product_event.objects.filter(events=event_id)
    autos = Auto_event.objects.filter(events=event_id)
    return render(request, 'events/event.html', {'events_list': events, 'inventory': inventory, 'products': products, 'autos': autos})
# Create your views here.
