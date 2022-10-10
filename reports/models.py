from django.db import models

from datetime import date, datetime, timedelta
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'police_{0}/{1}'.format(instance.police_id, filename)

def get_default_my_date():
  return date.today() - timedelta(days=25)

class PoliceRanks(models.TextChoices):
    IGP = 'IGP', _('আইজিপি')
    EIG = 'EIG', _('অতিঃ আইজি')
    DIG = 'DIG', _('ডিআইজি')
    EDIG = 'EDIG', _('অতিঃ ডিআইজি')
    SP = 'SP', _('এসপি')
    ESP = 'ESP', _('অতিঃ এসপি')
    SSP = 'SSP', _('সিনিয়র এসপি')
    ASP = 'ASP', _('এএসপি')
    I = 'I', _('ইন্সপেক্টর')
    SI = 'SI', _('এসআই')
    ASI = 'ASI', _('এএসআই')

# Create your models here.
class Police(models.Model):
    police_id = models.CharField(max_length=50, primary_key = True,
        verbose_name='ID')
    police_name_english = models.CharField(max_length=200,
        verbose_name='Name in English')
    police_name_bangla = models.CharField(max_length=200,
        verbose_name='Name in Bangla')
    police_rank = models.CharField(max_length=4, choices=PoliceRanks.choices, default=PoliceRanks.I,
        verbose_name='Rank')
    police_image = models.ImageField(upload_to = user_directory_path, default='logo.jpeg',
        verbose_name='Picture')
    police_dob = models.DateField(default=get_default_my_date,
        verbose_name='Date of Birth')
    police_created = models.DateTimeField(auto_now_add = True)
    police_updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.police_name_english