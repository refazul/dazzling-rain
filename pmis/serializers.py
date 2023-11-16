from rest_framework import serializers
from .models import Person, Address

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'  # Or list specific fields you want to include

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'  # Or list specific fields you want to include
