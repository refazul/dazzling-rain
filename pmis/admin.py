from django.contrib import admin
from .models import Person, Education, Posting, ServiceHistory, LocalTraining

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
    list_display = ('first_name', 'last_name', 'date_of_birth')  # Customize the columns displayed
    search_fields = ('first_name', 'last_name')  # Add search functionality
    list_filter = ('date_of_birth',)  # Add filter options
    inlines = [EducationInline, PostingInline, ServiceHistoryInline, LocalTrainingInline]

admin.site.register(Person, PersonAdmin)
