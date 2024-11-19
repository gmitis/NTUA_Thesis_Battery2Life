from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from batteries.models import EIS, Manufacturer, Battery, Module, Cell
from batteries.api.serializers import (
    EISSerializer,
    ManufacturerSerializer,
    BatteriesSerializer,
    ModuleSerializer,
    CellSerializer,
)
from batteries.mixins import LoggingMixin

class ManufacturerViewSet(
    LoggingMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class BatteriesViewSet(LoggingMixin, ModelViewSet):
    queryset = Battery.objects.all()
    serializer_class = BatteriesSerializer
    permission_classes = [IsAuthenticated]


class ModuleViewSet(LoggingMixin, ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]


class CellViewSet(LoggingMixin, ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    permission_classes = [IsAuthenticated]


class EISViewSet(LoggingMixin, ModelViewSet):
    queryset = EIS.objects.all()
    serializer_class = EISSerializer
    permission_classes = [IsAuthenticated]


class MeasumentViewSet():
    pass
