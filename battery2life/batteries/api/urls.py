from django.urls import path, include
from rest_framework.routers import DefaultRouter
from batteries.api.views import (ManufacturerViewSet, 
                                 BatteriesViewSet, MeasurementViewSet, 
                                 ModuleViewSet,
                                 CellViewSet,
                                 EISViewSet,
                                 ChemicalViewSet,
                                 SafetyFeatureViewSet,
                                 MaterialViewSet
                                 )

router = DefaultRouter()
router.register(r"safety_feature", SafetyFeatureViewSet)
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"measurements", MeasurementViewSet)
router.register(r"batteries", BatteriesViewSet)
router.register(r"chemical", ChemicalViewSet)
router.register(r"material", MaterialViewSet)
router.register(r"modules", ModuleViewSet)
router.register(r"cells", CellViewSet)
router.register(r"eis", EISViewSet)
urlpatterns = [
    path("", include(router.urls))
]