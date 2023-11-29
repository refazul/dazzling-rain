# serializers.py
from rest_framework import serializers
from .models import Person, Spouse, Permanent, Present, Child, Language, Education, Training, Travel, Abroad, Qualification, Publication, Honour, Other, Service, Promotion, Prosecution, Posting, Recent

class CustomDateField(serializers.DateField):
    def to_internal_value(self, data):
        if data == '':
            # Return None when the input is an empty string
            return None
        return super().to_internal_value(data)

class SpouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spouse
        fields = '__all__'

class PermanentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permanent
        fields = '__all__'

class PresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Present
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    date_of_birth = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Child
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class TrainingSerializer(serializers.ModelSerializer):
    from_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    to_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Training
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    from_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    to_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Travel
        fields = '__all__'

class AbroadSerializer(serializers.ModelSerializer):
    from_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    to_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Abroad
        fields = '__all__'

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    date = CustomDateField(required=False, input_formats=["%Y-%m-%d"])

    class Meta:
        model = Publication
        fields = '__all__'

class HonourSerializer(serializers.ModelSerializer):
    date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Honour
        fields = '__all__'

class OtherSerializer(serializers.ModelSerializer):
    from_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    to_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Other
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    govt_service_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    gazetted_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    encadrement_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Service
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    promotion_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    g_o_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Promotion
        fields = '__all__'

class ProsecutionSerializer(serializers.ModelSerializer):
    date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Prosecution
        fields = '__all__'

class PostingSerializer(serializers.ModelSerializer):
    from_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    to_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Posting
        fields = '__all__'

class RecentSerializer(serializers.ModelSerializer):
    order_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    join_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    release_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Recent
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    spouse = SpouseSerializer(many=True, read_only=True)
    permanent = PermanentSerializer(many=True, read_only=True)
    present = PresentSerializer(many=True, read_only=True)
    child = ChildSerializer(many=True, read_only=True)
    language = LanguageSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    training = TrainingSerializer(many=True, read_only=True)
    travel = TravelSerializer(many=True, read_only=True)
    abroad = AbroadSerializer(many=True, read_only=True)
    qualification = QualificationSerializer(many=True, read_only=True)
    publication = PublicationSerializer(many=True, read_only=True)
    honour = HonourSerializer(many=True, read_only=True)
    other = OtherSerializer(many=True, read_only=True)
    service = ServiceSerializer(many=True, read_only=True)
    promotion = PromotionSerializer(many=True, read_only=True)
    prosecution = ProsecutionSerializer(many=True, read_only=True)
    posting = PostingSerializer(many=True, read_only=True)
    recent = RecentSerializer(many=True, read_only=True)

    date_of_birth = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    join_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    lpr_prl_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    order_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    cadre_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])
    confirmation_g_o_date = CustomDateField(required=False, input_formats=["%d/%m/%y"])

    class Meta:
        model = Person
        fields = '__all__'