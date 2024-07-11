from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136366ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136366", Testconnectors136366ViewSet, basename="testconnectors136366"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
