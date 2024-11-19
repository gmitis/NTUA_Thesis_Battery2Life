from django.urls import path, include
from rest_framework.routers import DefaultRouter
from batteries.api.views import (ManufacturerViewSet, 
                                 BatteriesViewSet, 
                                 ModuleViewSet,
                                 CellViewSet,
                                 EISViewSet
                                 )

router = DefaultRouter()
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"batteries", BatteriesViewSet)
router.register(r"modules", ModuleViewSet)
router.register(r"cells", CellViewSet)
router.register(r"eis", EISViewSet)

urlpatterns = [
    path("", include(router.urls))
]