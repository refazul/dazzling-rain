from django.contrib import admin
from .models import Person, Education, Posting, ServiceHistory, LocalTraining

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')  # Customize the columns displayed
    search_fields = ('first_name', 'last_name')  # Add search functionality
    list_filter = ('date_of_birth',)  # Add filter options

admin.site.register(Person, PersonAdmin)
admin.site.register(Education)
admin.site.register(Posting)
admin.site.register(ServiceHistory)
admin.site.register(LocalTraining)

