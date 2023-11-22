# serializers.py
from rest_framework import serializers
from .models import Person, Child, Spouse, Address, Education, Training, Posting

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

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    child = ChildSerializer(many=True, read_only=True)
    spouse = SpouseSerializer(many=True, read_only=True)
    address = AddressSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    training = TrainingSerializer(many=True, read_only=True)
    posting = PostingSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'