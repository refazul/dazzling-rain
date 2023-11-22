from django.contrib import admin
from .models import Person,Spouse, Child, Address, Language, Education, Training, Travel, PostingAbroad, AdditionalProQualification, Publication, HonourAward, OtherServices, ServiceHistory, PromotionParticulars, DisciplinaryActions, Posting

class SpouseInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Spouse
    extra = 1  # Number of empty forms to display

class AddressInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Address
    extra = 1  # Number of empty forms to display

class ChildInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Child
    extra = 1  # Number of empty forms to display

class LanguageInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Language
    extra = 1

class EducationInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Education
    extra = 1  # Number of empty forms to display

class TrainingInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Training
    extra = 1  # Number of empty forms to display

class TravelInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Travel
    extra = 1  # Number of empty forms to display

class PostingAbroadInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = PostingAbroad
    extra = 1  # Number of empty forms to display

class AdditionalProQualificationInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = AdditionalProQualification
    extra = 1  # Number of empty forms to display


class PublicationInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Publication
    extra = 1  # Number of empty forms to display

class HonourAwardInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = HonourAward
    extra = 1  # Number of empty forms to display

class OtherServicesInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = OtherServices
    extra = 1  # Number of empty forms to display

class ServiceHistoryInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = ServiceHistory
    extra = 1  # Number of empty forms to display

class PromotionParticularsInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = PromotionParticulars
    extra = 1  # Number of empty forms to display

class DisciplinaryActionsInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = DisciplinaryActions
    extra = 1  # Number of empty forms to display

class PostingInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Posting
    extra = 1  # Number of empty forms to display

class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'nid', 'govt_id')  # Customize the columns displayed
    search_fields = ('person_name', 'nid', 'govt_id')  # Add search functionality
    list_filter = ('rank', 'batch', 'home_district')  # Add filter options
    fieldsets = [
        ('Basic', {'fields': [
            'govt_id',
            'person_name',
            'name_bangla',
            'father_name',
            'mother_name',
            'date_of_birth',
            'lpr_prl_date',
            'rank',
            'home_district',
            'designation',
            'organisation',
            'order_date',
            'join_date',
            'cadre',
            'cadre_date',
            'batch',
            'confirmation_g_o_date',
            'gender',
            'religion',
            'marital_stat',
            'nid',
            'freedom_fighter',
            'mobile',
            'email',
        ]}),
    ]
    inlines = [SpouseInline, ChildInline, AddressInline, LanguageInline, EducationInline, TrainingInline, TravelInline, PostingAbroadInline, AdditionalProQualificationInline, PublicationInline, HonourAwardInline, OtherServicesInline, ServiceHistoryInline, PromotionParticularsInline, DisciplinaryActionsInline, PostingInline]

admin.site.register(Person, PersonAdmin)
