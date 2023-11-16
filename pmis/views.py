from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Person, Address
from .serializers import PersonSerializer, AddressSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
