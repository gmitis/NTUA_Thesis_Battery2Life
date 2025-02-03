from django.contrib import admin
from .models import EIS, Cell, Manufacturer, Battery, Measurement, Module, Address, Dimension, Chemical, SafetyFeature, Material

admin.site.register(Manufacturer)
admin.site.register(Battery)
admin.site.register(Module)
admin.site.register(Cell)
admin.site.register(Measurement)
admin.site.register(EIS)
admin.site.register(Dimension)
admin.site.register(Chemical)
admin.site.register(SafetyFeature)
admin.site.register(Material)
admin.site.register(Address)
