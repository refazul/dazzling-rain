from django.db import models
from django.utils.translation import gettext_lazy as _

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
    def __str__(self):
        return self.police_name_english