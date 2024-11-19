from rest_framework import serializers
from batteries.models import EIS, Manufacturer, Battery, Measurement, Module, Cell


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"


class BatteriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Battery
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"
        


class CellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cell
        fields = "__all__"
        
class EISSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EIS
        fields = "__all__"

class MeasurementsSerializer(serializers.ModelSerializer):
    pass