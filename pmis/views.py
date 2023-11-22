from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from .models import Person, Address, Spouse, Child, Education, Training, Posting
from .serializers import PersonSerializer, AddressSerializer, SpouseSerializer, ChildSerializer, EducationSerializer, TrainingSerializer, PostingSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=govt_id']

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class SpouseViewSet(viewsets.ModelViewSet):
    queryset = Spouse.objects.all()
    serializer_class = SpouseSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
