from rest_framework import serializers
from batteries.models import Manufacturer, Batteries

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"


class BatteriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batteries
        fields = "__all__"