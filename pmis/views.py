from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from .models import Person, Spouse, Permanent, Present, Child, Language, Education, Training, Travel, Abroad, Qualification, Publication, Honour, Other, Service, Promotion, Prosecution, Posting
from .serializers import PersonSerializer, SpouseSerializer, PermanentSerializer, PresentSerializer, ChildSerializer, LanguageSerializer, EducationSerializer, TrainingSerializer, TravelSerializer, AbroadSerializer, QualificationSerializer, PublicationSerializer, HonourSerializer, OtherSerializer, ServiceSerializer, PromotionSerializer, ProsecutionSerializer, PostingSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=govt_id']

class SpouseViewSet(viewsets.ModelViewSet):
    queryset = Spouse.objects.all()
    serializer_class = SpouseSerializer

class PermanentViewSet(viewsets.ModelViewSet):
    queryset = Permanent.objects.all()
    serializer_class = PermanentSerializer

class PresentViewSet(viewsets.ModelViewSet):
    queryset = Present.objects.all()
    serializer_class = PresentSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class AbroadViewSet(viewsets.ModelViewSet):
    queryset = Abroad.objects.all()
    serializer_class = AbroadSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class HonourViewSet(viewsets.ModelViewSet):
    queryset = Honour.objects.all()
    serializer_class = HonourSerializer

class OtherViewSet(viewsets.ModelViewSet):
    queryset = Other.objects.all()
    serializer_class = OtherSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class ProsecutionViewSet(viewsets.ModelViewSet):
    queryset = Prosecution.objects.all()
    serializer_class = ProsecutionSerializer

class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer