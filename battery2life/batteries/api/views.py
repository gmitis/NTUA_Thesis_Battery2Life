from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from batteries.models import Manufacturer, Batteries, Module, Cell
from batteries.api.serializers import (ManufacturerSerializer, 
                                       BatteriesSerializer, 
                                       ModuleSerializer, 
                                       CellSerializer)


class ManufacturerViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class BatteriesViewSet(ModelViewSet):
    queryset = Batteries.objects.all()
    serializer_class = BatteriesSerializer
    permission_classes = [IsAuthenticated]

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsAuthenticated]

class CellViewSet(ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    permission_classes = [IsAuthenticated]