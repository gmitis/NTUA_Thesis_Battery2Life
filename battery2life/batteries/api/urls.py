from django.urls import path, include
from rest_framework.routers import DefaultRouter
from batteries.api.views import ManufacturerViewSet, BatteriesViewSet

router = DefaultRouter()
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"batteries", BatteriesViewSet)

urlpatterns = [
    path("", include(router.urls))
]