from django.contrib import admin

from django.contrib import admin

from .models import Events, Inventary_event, Product_event, Auto_event

admin.site.register(Events)
admin.site.register(Inventary_event)
admin.site.register(Product_event)
admin.site.register(Auto_event)

# Register your models here.
