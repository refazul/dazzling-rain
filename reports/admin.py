from django.contrib import admin
from django_object_actions import DjangoObjectActions
from django.shortcuts import redirect

# Register your models here.
from .models import Police

from django import forms
class PoliceForm(forms.ModelForm):
    police_category = forms.ChoiceField(choices=[('A','A'), ('B','B'), ('C', 'C')], widget=forms.RadioSelect, label='Category')
    police_address_permanent = forms.CharField(widget=forms.Textarea, required=False, label='স্থায়ী ঠিকানা')
    police_address_present = forms.CharField(widget=forms.Textarea, required=False, label='বর্তমান ঠিকানা')
    police_past = forms.CharField(widget=forms.Textarea, required=False, label='পূর্ববর্তী কর্মস্থল সমূহ')
    police_family_background = forms.CharField(widget=forms.Textarea, required=False, label='পারিবারিক ইতিহাস')
    police_political_background = forms.CharField(widget=forms.Textarea, required=False, label='রাজনৈতিক ইতিহাস')
    police_comments = forms.CharField(widget=forms.Textarea, required=False, label='পর্যবেক্ষণ মন্তব্য')
    class Meta:
        model = Police
        fields = ['police_address_permanent', 'police_address_present', 'police_past', 'police_family_background', 'police_political_background', 'police_comments']

# Register your models here.
class PoliceAdmin(DjangoObjectActions, admin.ModelAdmin):
    def pdf_this(self, request, obj):
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(f'/pdf/{obj.police_id}')
    pdf_this.label = "Download PDF"  # optional
    pdf_this.short_description = "Download the PDF"  # optional

    change_actions = ('pdf_this', )
    fieldsets = [
        ('Basic', {'fields': [
                                'police_name_bangla',
                                'police_name_english',
                                'police_id',
                                'police_rank',
                                'police_designation',
                                'police_present',
                                'police_image'
                                'police_image_url'
                            ]}),
        ('Section 2', {'fields': [
                                'police_father',
                                'police_mother',
                                'police_spouse',
                                'police_gender',
                                'police_nid',
                                'police_district',
                                'police_address_permanent',
                                'police_address_present',
                                'police_dob',
                                'police_batch',
                                'police_merit',
                                'police_joining_rank',
                                'police_category'
                            ]}),
        ('Section 3', {'fields': [
                                'police_blood_group',
                                'police_religion',
                                'police_mobile',
                                'police_email',
                                'police_present_status',
                                'police_edu',
                                'police_past',
                                'police_family_background',
                                'police_political_background',
                                'police_comments'
                            ]}),
    ]
    list_display = ('police_id', 'police_batch', 'police_merit', 'police_name_bangla', 'police_rank', 'police_district')
    search_fields = ['police_id']
    form = PoliceForm

admin.site.register(Police, PoliceAdmin)