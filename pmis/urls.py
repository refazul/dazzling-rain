from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, AddressViewSet, SpouseViewSet, ChildViewSet, EducationViewSet, TrainingViewSet, PostingViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'spouses', SpouseViewSet)
router.register(r'children', ChildViewSet)
router.register(r'education', EducationViewSet)
router.register(r'training', TrainingViewSet)
router.register(r'posting', PostingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
