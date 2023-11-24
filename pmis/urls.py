from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, SpouseViewSet, PermanentViewSet, PresentViewSet, ChildViewSet, LanguageViewSet, EducationViewSet, TrainingViewSet, TravelViewSet, AbroadViewSet, QualificationViewSet, PublicationViewSet, HonourViewSet, OtherViewSet, ServiceViewSet, PromotionViewSet, ProsecutionViewSet, PostingViewSet, RecentViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'spouse', SpouseViewSet)
router.register(r'permanent', PermanentViewSet)
router.register(r'present', PresentViewSet)
router.register(r'child', ChildViewSet)
router.register(r'language', LanguageViewSet)
router.register(r'education', EducationViewSet)
router.register(r'training', TrainingViewSet)
router.register(r'travel', TravelViewSet)
router.register(r'abroad', AbroadViewSet)
router.register(r'qualification', QualificationViewSet)
router.register(r'publication', PublicationViewSet)
router.register(r'honour', HonourViewSet)
router.register(r'other', OtherViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'promotion', PromotionViewSet)
router.register(r'prosecution', ProsecutionViewSet)
router.register(r'posting', PostingViewSet)
router.register(r'recent', RecentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
