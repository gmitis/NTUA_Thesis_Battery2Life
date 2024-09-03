from rest_framework import serializers
from batteries.models import Manufacturer, Batteries, Module

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"


class BatteriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batteries
        fields = "__all__"

class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"