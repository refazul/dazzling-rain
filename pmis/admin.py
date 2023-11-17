from django.contrib import admin
from .models import Person, Education, Posting, ServiceHistory, LocalTraining, Child, Spouse,Address

class ChildInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Child
    extra = 1  # Number of empty forms to display

class SpouseInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Spouse
    extra = 1  # Number of empty forms to display

class AddressInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Address
    extra = 1  # Number of empty forms to display

class EducationInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Education
    extra = 1  # Number of empty forms to display

class PostingInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Posting
    extra = 1  # Number of empty forms to display

class ServiceHistoryInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = ServiceHistory
    extra = 1  # Number of empty forms to display

class LocalTrainingInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = LocalTraining
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
            'organization',
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
            'mobile',
            'email',
        ]}),
    ]
    inlines = [ChildInline, SpouseInline, AddressInline, EducationInline, PostingInline, ServiceHistoryInline, LocalTrainingInline]

admin.site.register(Person, PersonAdmin)
