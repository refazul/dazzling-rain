# serializers.py
from rest_framework import serializers
from .models import Person, Child, Spouse, Address

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class SpouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spouse
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    child = ChildSerializer(many=True)
    spouse = SpouseSerializer(many=True)
    address = AddressSerializer(many=True)

    class Meta:
        model = Person
        fields = '__all__'
