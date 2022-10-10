from django.db import models

from datetime import date, datetime, timedelta
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'police_{0}/{1}'.format(instance.police_id, filename)

def get_default_dob():
  return datetime(1980, 1, 1)

def get_default_my_date():
  return date.today() - timedelta(days=25)

class PoliceRanks(models.TextChoices):
    IGP = 'IGP', _('আইজিপি')
    AddlIG = 'Addl. IG', _('অতিঃ আইজি')
    DIG = 'DIG', _('ডিআইজি')
    AddlDIG = 'Addl. DIG', _('অতিঃ ডিআইজি')
    SP = 'SP', _('এসপি')
    AddlSP = 'Addl. SP', _('অতিঃ এসপি')
    SrSP = 'Sr. SP', _('সিনিয়র এসপি')
    ASP = 'ASP', _('এএসপি')
    SrASP = 'Sr. ASP', _('সিনিয়র এএসপি')
    I = 'I', _('ইন্সপেক্টর')
    SI = 'SI', _('এসআই')
    ASI = 'ASI', _('এএসআই')
    NA = 'NA', _('প্রযোজ্য নহে')

# Create your models here.
class Police(models.Model):
    # Texts
    police_id = models.CharField(max_length=50, primary_key = True,
        verbose_name='ID')
    police_name_english = models.CharField(max_length=200,
        verbose_name='Name in English')
    police_name_bangla = models.CharField(max_length=200,
        verbose_name='Name in Bangla')
    
    # Selects
    police_rank = models.CharField(max_length=10, choices=PoliceRanks.choices, default=PoliceRanks.NA,
        verbose_name='Rank')
    
    # Media
    police_image = models.ImageField(upload_to = user_directory_path, default='logo.jpeg',
        verbose_name='Picture')
    
    # Dates
    police_dob = models.DateField(default=get_default_dob,
        verbose_name='Date of Birth')
    @admin.display(
        description='Age',
        ordering='police_dob',
    )
    def police_age(self):
        return str(date.today() - self.police_dob).split(',')[0]
    
    # Timestamps
    police_created = models.DateTimeField(auto_now_add = True)
    police_updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.police_name_english