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
        

class AddMeasurementSerializer(serializers.Serializer):
    cell_ids = serializers.ListField(
        child=serializers.IntegerField(), 
        min_length=4, 
        max_length=4
    )

    voltage = serializers.ListField(
        child=serializers.FloatField(), 
        min_length=4, 
        max_length=4
    )

    temperature = serializers.ListField(
        child=serializers.FloatField(), 
        min_length=4, 
        max_length=4
    )

    current = serializers.ListField(
        child=serializers.FloatField(), 
        min_length=4, 
        max_length=4
    )

    sot = serializers.ListField(
        child=serializers.FloatField(), 
        min_length=4, 
        max_length=4
    )

    phase = serializers.ListField(
        child=serializers.FloatField(), 
        min_length=4, 
        max_length=4
    )

    soc = serializers.ListField(
        child=serializers.FloatField(), 
        min_length=4, 
        max_length=4
    )

    def validate_cell_ids(self, value):
        queryset = Cell.objects.values_list('id')
        registered_ids = [item[0] for item in queryset]
        for candidate_id in value:
            if candidate_id < 0:
                raise serializers.ValidationError("cell_id field must be a positive integer number")
            if candidate_id not in registered_ids:
                raise serializers.ValidationError(f"Cell instance with cell_id: {candidate_id} must already exist, please create Cell instance")
        return value

        
class EISSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EIS
        fields = "__all__"
    
    
    
class MeasurementsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Measurement
        fields = '__all__'