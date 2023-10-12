from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='events_index'),
    path('<int:event_id>/', views.event, name='events_event'),
    # path('create/', views.events_create, name='event_create'),
    # path('calendar/', views.calendar, name='calendar'),
]
