from django.contrib import admin
from .models import EIS, Cell, Manufacturer, Battery, Measurement, Module

admin.site.register(Manufacturer)
admin.site.register(Battery)
admin.site.register(Module)
admin.site.register(Cell)
admin.site.register(Measurement)
admin.site.register(EIS)
