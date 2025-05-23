# todo: is there a better way to write MeasurementViewSet create method?

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from batteries.api import serializers
from batteries.models import EIS, Manufacturer, Battery, Measurement, Module, Cell, Chemical, SafetyFeature, Material
from batteries.api.serializers import (
    EISSerializer,
    ManufacturerSerializer,
    BatteriesSerializer,
    MeasurementsSerializer,
    AddMeasurementSerializer,
    ModuleSerializer,
    CellSerializer,
    ChemicalSerializer,
    SafetyFeatureSerializer,
    MaterialSerializer
)
from batteries.mixins import LoggingMixin


class ChemicalViewSet(LoggingMixin, ModelViewSet):
    queryset = Chemical.objects.all()
    serializer_class = ChemicalSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    
class SafetyFeatureViewSet(LoggingMixin, ModelViewSet):
    queryset = SafetyFeature.objects.all()
    serializer_class = SafetyFeatureSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class MaterialViewSet(LoggingMixin, ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    

class ManufacturerViewSet(LoggingMixin, ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class BatteriesViewSet(LoggingMixin, ModelViewSet):
    queryset = Battery.objects.all()
    serializer_class = BatteriesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ModuleViewSet(LoggingMixin, ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CellViewSet(LoggingMixin, ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    

class EISViewSet(LoggingMixin, ModelViewSet):
    queryset = EIS.objects.all()
    serializer_class = EISSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class MeasurementViewSet(LoggingMixin, ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # Save real time measurement data 
    def create(self, request, *args, **kwargs):
        serializer = serializers.AddMeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        cell_id = serializer.validated_data.get("cell_ids")
        voltage = serializer.validated_data.get("voltage")
        temperature = serializer.validated_data.get("temperature")
        current = serializer.validated_data.get("current")
        sot = serializer.validated_data.get("sot")
        phase = serializer.validated_data.get("phase")
        soc = serializer.validated_data.get("soc")
        
        for id in range(4):
            cell = Cell.objects.get(id=cell_id[id])
            Measurement.objects.create(
                cell_id=cell, 
                voltage=voltage[id], 
                temperature=temperature[id], 
                current=current[id], 
                sot=sot[id], 
                phase=phase[id], 
                soc=soc[id]
            )
            
        return Response(serializer.data, status=status.HTTP_200_OK)
