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
        

class AddCellSerializer(serializers.Serializer):
    cell_id = serializers.ListField(child=serializers.IntegerField(), allow_empty=False)

    def validate_cell_ids(self, value):
        # validate for duplicates
        if len(value) != len(set(value)):
            raise serializers.ValidationError("Please remove duplicate ids from your request")
        if len(value) != len(list(filter(lambda x:x>=0, value))):
            raise serializers.ValidationError("All ids must be positive integer numbers")
        return value


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