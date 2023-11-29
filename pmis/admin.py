from django.contrib import admin
from .models import Person, Spouse, Child, Permanent, Present, Language, Education, Training, Travel, Abroad, Qualification, \
    Publication, Honour, Other, Service, Promotion, Prosecution, Posting, Recent
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse
from django.urls import path
import csv

class SpouseInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Spouse
    extra = 1  # Number of empty forms to display


class PermanentInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Permanent
    extra = 1  # Number of empty forms to display

class PresentInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Present
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


class AbroadInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Abroad
    extra = 1  # Number of empty forms to display


class QualificationInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Qualification
    extra = 1  # Number of empty forms to display


class PublicationInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Publication
    extra = 1  # Number of empty forms to display


class HonourInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Honour
    extra = 1  # Number of empty forms to display


class OtherInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Other
    extra = 1  # Number of empty forms to display


class ServiceInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Service
    extra = 1  # Number of empty forms to display


class PromotionInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Promotion
    extra = 1  # Number of empty forms to display


class ProsecutionInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Prosecution
    extra = 1  # Number of empty forms to display


class PostingInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Posting
    ordering = ("from_date", 'to_date',)
    extra = 1  # Number of empty forms to display

class RecentInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Recent
    ordering = ("order_date",)
    extra = 1  # Number of empty forms to display

class PersonAdmin(DjangoObjectActions, admin.ModelAdmin):
    # Export As CSV
    actions = ["export_as_csv"]
    def export_as_csv(self, request, queryset):
        """
        Export the current queryset as CSV.
        """
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export as CSV"

    def pdf_this(self, request, obj):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(f'/pmis/{obj.id}')

    pdf_this.label = "Download PDF"  # optional
    pdf_this.short_description = "Download the PDF"  # optional

    change_actions = ('pdf_this',)

    list_display = ('person_name', 'name_bangla', 'nid', 'govt_id')  # Customize the columns displayed
    search_fields = ('person_name', 'nid', 'govt_id')  # Add search functionality
    list_filter = ('rank', 'batch', 'home_district', 'designation', 'organisation')  # Add filter options
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
    inlines = [SpouseInline, ChildInline, PermanentInline, PresentInline, LanguageInline, EducationInline, TrainingInline, TravelInline,
               AbroadInline, QualificationInline, PublicationInline, HonourInline, OtherInline, ServiceInline, PromotionInline,
               ProsecutionInline, PostingInline, RecentInline]

admin.site.register(Person, PersonAdmin)
