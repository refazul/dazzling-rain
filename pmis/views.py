from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from .models import Person, Spouse, Permanent, Present, Child, Language, Education, Training, Travel, Abroad, Qualification, Publication, Honour, Other, Service, Promotion, Prosecution, Posting
from .serializers import PersonSerializer, SpouseSerializer, PermanentSerializer, PresentSerializer, ChildSerializer, LanguageSerializer, EducationSerializer, TrainingSerializer, TravelSerializer, AbroadSerializer, QualificationSerializer, PublicationSerializer, HonourSerializer, OtherSerializer, ServiceSerializer, PromotionSerializer, ProsecutionSerializer, PostingSerializer
from wkhtmltopdf.views import PDFTemplateView
from django.views.generic import TemplateView

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


class PmisPDF(PDFTemplateView):
    # filename = 'pdf.pdf'
    template_name = 'pmis.html'
    show_content_in_browser = True
    model = Person
    cmd_options = {
        'margin-top': 3
    }

    def get_filename(self, **kwargs):
        return self.kwargs['pmis_id'] + '.pdf'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pmis_id = self.kwargs['pmis_id']
        pmis_person = Person.objects.get(pk=pmis_id)

        context['id'] = pmis_id
        context['govt_id'] = getattr(pmis_person, 'govt_id')
        context['person_name'] = getattr(pmis_person, 'person_name')
        context['name_bangla'] = getattr(pmis_person, 'name_bangla')
        context['father_name'] = getattr(pmis_person, 'father_name')
        context['mother_name'] = getattr(pmis_person, 'mother_name')
        context['gender'] = getattr(pmis_person, 'gender')
        context['freedom_fighter'] = getattr(pmis_person, 'freedom_fighter')
        context['date_of_birth'] = getattr(pmis_person, 'date_of_birth')
        context['lpr_prl_date'] = getattr(pmis_person, 'lpr_prl_date')
        context['order_date'] = getattr(pmis_person, 'order_date')
        context['join_date'] = getattr(pmis_person, 'join_date')
        context['cadre_date'] = getattr(pmis_person, 'cadre_date')
        context['confirmation_g_o_date'] = getattr(pmis_person, 'confirmation_g_o_date')
        context['rank'] = getattr(pmis_person, 'rank')
        context['home_district'] = getattr(pmis_person, 'home_district')
        context['designation'] = getattr(pmis_person, 'designation')
        context['organisation'] = getattr(pmis_person, 'organisation')
        context['cadre'] = getattr(pmis_person, 'cadre')
        context['batch'] = getattr(pmis_person, 'batch')
        context['religion'] = getattr(pmis_person, 'religion')
        context['marital_stat'] = getattr(pmis_person, 'marital_stat')
        context['nid'] = getattr(pmis_person, 'nid')
        context['mobile'] = getattr(pmis_person, 'mobile')
        context['email'] = getattr(pmis_person, 'email')

        context['spouse'] = pmis_person.spouse.first()
        context['permanent'] = pmis_person.permanent.first()
        context['present'] = pmis_person.present.first()
        context['child'] = pmis_person.child.all()
        context['language'] = pmis_person.language.all()
        context['education'] = pmis_person.education.all().order_by('passing_year')
        context['training_local_mandatory'] = pmis_person.training.filter(training_type='LM').order_by('from_date')
        context['training_local'] = pmis_person.training.filter(training_type='L').order_by('from_date')
        context['training_foreign'] = pmis_person.training.filter(training_type='F').order_by('from_date')
        context['travel'] = pmis_person.travel.all().order_by('from_date')
        context['abroad'] = pmis_person.abroad.all().order_by('from_date')
        context['qualification'] = pmis_person.qualification.all()
        context['publication'] = pmis_person.publication.all().order_by('date')
        context['honour'] = pmis_person.honour.all().order_by('date')
        context['other'] = pmis_person.other.all().order_by('from_date')
        context['service'] = pmis_person.service.all().order_by('govt_service_date')
        context['promotion'] = pmis_person.promotion.all().order_by('promotion_date')
        context['prosecutioin'] = pmis_person.prosecution.all().order_by('date')
        context['posting'] = pmis_person.posting.all().order_by('from_date')


        return context