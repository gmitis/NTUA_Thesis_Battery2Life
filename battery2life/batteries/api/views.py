from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from batteries.models import Manufacturer, Batteries
from batteries.api.serializers import ManufacturerSerializer, BatteriesSerializer


class ManufacturerViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]


class BatteriesViewSet(ModelViewSet):
    queryset = Batteries.objects.all()
    serializer_class = BatteriesSerializer
    permission_classes = [IsAuthenticated]