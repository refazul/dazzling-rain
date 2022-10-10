from django.db import models

import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'police_{0}/{1}'.format(instance.police_id, filename)

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
    police_id = models.CharField(max_length=50, primary_key = True)
    police_name_english = models.CharField(max_length=200)
    police_name_bangla = models.CharField(max_length=200)
    police_rank = models.CharField(
        max_length=4,
        choices=PoliceRanks.choices,
        default=PoliceRanks.I,
    )
    police_image = models.ImageField(upload_to = user_directory_path, default='static/logo.jpeg')
    def __str__(self):
        return self.police_name_english