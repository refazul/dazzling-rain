from django.contrib import admin

# Register your models here.
from .models import Police

# Register your models here.
class PoliceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic', {'fields': ['police_id', 'police_name_english', 'police_name_bangla', 'police_image']}),
        ('Status', {'fields': ['police_rank']}),
    ]
    list_display = ('police_id', 'police_name_bangla', 'police_rank')
    search_fields = ['police_id']

admin.site.register(Police, PoliceAdmin)