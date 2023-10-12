from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='auto_index'),
    # path('<int:event>/edit/', views.events_edit, name='event_edit'),
    # path('create/', views.events_create, name='event_create'),
    # path('calendar/', views.calendar, name='calendar'),
]
