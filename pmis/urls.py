from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, AddressViewSet, SpouseViewSet, ChildViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'spouses', SpouseViewSet)
router.register(r'children', ChildViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
