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
  return date.today() - timedelta(days=3650)
class Districts(models.TextChoices):
    Comilla = 'কুমিল্লা', _('কুমিল্লা')
    Feni = 'ফেনী', _('ফেনী')
    Brahmanbaria = 'ব্রাহ্মণবাড়িয়া', _('ব্রাহ্মণবাড়িয়া')
    Rangamati = 'রাঙ্গামাটি', _('রাঙ্গামাটি')
    Noakhali = 'নোয়াখালী', _('নোয়াখালী')
    Chandpur = 'চাঁদপুর', _('চাঁদপুর')
    Lakshmipur = 'লক্ষ্মীপুর', _('লক্ষ্মীপুর')
    Chittagong = 'চট্টগ্রাম', _('চট্টগ্রাম')
    CoxBazar = 'কক্সবাজার', _('কক্সবাজার')
    Khagrachhari = 'খাগড়াছড়ি', _('খাগড়াছড়ি')
    Bandarban = 'বান্দরবান', _('বান্দরবান')
    Sirajganj = 'সিরাজগঞ্জ', _('সিরাজগঞ্জ')
    Pabna = 'পাবনা', _('পাবনা')
    Bogra = 'বগুড়া', _('বগুড়া')
    Rajshahi = 'রাজশাহী', _('রাজশাহী')
    Natore = 'নাটোর', _('নাটোর')
    Joypurhat = 'জয়পুরহাট', _('জয়পুরহাট')
    ChapaiNawabganj = 'চাঁপাইনবাবগঞ্জ', _('চাঁপাইনবাবগঞ্জ')
    Naogaon = 'নওগাঁ', _('নওগাঁ')
    Jessore = 'যশোর', _('যশোর')
    Satkhira = 'সাতক্ষীরা', _('সাতক্ষীরা')
    Meherpur = 'মেহেরপুর', _('মেহেরপুর')
    Narail = 'নড়াইল', _('নড়াইল')
    Chuadanga = 'চুয়াডাঙ্গা', _('চুয়াডাঙ্গা')
    Kushtia = 'কুষ্টিয়া', _('কুষ্টিয়া')
    Magura = 'মাগুরা', _('মাগুরা')
    Khulna = 'খুলনা', _('খুলনা')
    Bagerhat = 'বাগেরহাট', _('বাগেরহাট')
    Jhenaidah = 'ঝিনাইদহ', _('ঝিনাইদহ')
    Jhalokati = 'ঝালকাঠি', _('ঝালকাঠি')
    Patuakhali = 'পটুয়াখালী', _('পটুয়াখালী')
    Pirojpur = 'পিরোজপুর', _('পিরোজপুর')
    Barisal = 'বরিশাল', _('বরিশাল')
    Bhola = 'ভোলা', _('ভোলা')
    Barguna = 'বরগুনা', _('বরগুনা')
    Sylhet = 'সিলেট', _('সিলেট')
    Moulvibazar = 'মৌলভীবাজার', _('মৌলভীবাজার')
    Habiganj = 'হবিগঞ্জ', _('হবিগঞ্জ')
    Sunamganj = 'সুনামগঞ্জ', _('সুনামগঞ্জ')
    Narsingdi = 'নরসিংদী', _('নরসিংদী')
    Gazipur = 'গাজীপুর', _('গাজীপুর')
    Shariatpur = 'শরীয়তপুর', _('শরীয়তপুর')
    Narayanganj = 'নারায়ণগঞ্জ', _('নারায়ণগঞ্জ')
    Tangail = 'টাঙ্গাইল', _('টাঙ্গাইল')
    Kishoreganj = 'কিশোরগঞ্জ', _('কিশোরগঞ্জ')
    Manikganj = 'মানিকগঞ্জ', _('মানিকগঞ্জ')
    Dhaka = 'ঢাকা', _('ঢাকা')
    Munshiganj = 'মুন্সিগঞ্জ', _('মুন্সিগঞ্জ')
    Rajbari = 'রাজবাড়ী', _('রাজবাড়ী')
    Madaripur = 'মাদারীপুর', _('মাদারীপুর')
    Gopalganj = 'গোপালগঞ্জ', _('গোপালগঞ্জ')
    Faridpur = 'ফরিদপুর', _('ফরিদপুর')
    Panchagar = 'পঞ্চগড়', _('পঞ্চগড়')
    Dinajpur = 'দিনাজপুর', _('দিনাজপুর')
    Lalmonirhat = 'লালমনিরহাট', _('লালমনিরহাট')
    Nilphamari = 'নীলফামারী', _('নীলফামারী')
    Gaibandha = 'গাইবান্ধা', _('গাইবান্ধা')
    Thakurgaon = 'ঠাকুরগাঁও', _('ঠাকুরগাঁও')
    Rangpur = 'রংপুর', _('রংপুর')
    Kurigram = 'কুড়িগ্রাম', _('কুড়িগ্রাম')
    Sherpur = 'শেরপুর', _('শেরপুর')
    Mymensingh = 'ময়মনসিংহ', _('ময়মনসিংহ')
    Jamalpur = 'জামালপুর', _('জামালপুর')
    Netrokona = 'নেত্রকোণা', _('নেত্রকোণা')
class Genders(models.TextChoices):
    Male = 'Male', _('পুরুষ')
    Female = 'Female', _('মহিলা')
class BloodGroups(models.TextChoices):
    Ap = 'A+', _('A+')
    An = 'A-', _('A-')
    Bp = 'B+', _('B+')
    Bn = 'B-', _('B-')
    ABp = 'AB+', _('AB+')
    ABn = 'AB-', _('AB-')
    Op = 'O+', _('O+')
    On = 'O-', _('O-')
class Religions(models.TextChoices):
    Islam = 'Islam', _('ইসলাম')
    Hindu = 'Hindu', _('হিন্দু')
    Christian = 'Christian', _('খ্রিস্টান')
    Buddha = 'Buddha', _('বৌদ্ধ')
    Others = 'Others', _('অন্যান্য')
class Batches(models.TextChoices):
    Seven = '7', _('7')
    Eight = '8', _('8')
    Twelve = '12', _('12')
    Fifteen = '15', _('15')
    Seventeen = '17', _('17')
    Eighteen = '18', _('18')
    Twenty = '20', _('20')
    TwentyOne = '21', _('21')
    TwentyTwo = '22', _('22')
    TwentyFour = '24', _('24')
    TwentyFive = '25', _('25')
    TwentySeven = '27', _('27')
    TwentyEight = '28', _('28')
    TwentyNine = '29', _('29')
    Thirty = '30', _('30')
    ThirtyOne = '31', _('31')
    ThirtyThree = '33', _('33')
    ThirtyFour = '34', _('34')
    ThirtyFive = '35', _('35')
    ThirtySix = '36', _('36')
class PresentStatus(models.TextChoices):
    OnJob = 'On Job', _('চাকুরীরত')
    Sacked = 'Sacked', _('চাকুরীচ্যুত')
    Retired = 'Retired', _('অবসরপ্রাপ্ত')
class JoiningRanks(models.TextChoices):
    ASP = 'ASP', _('এএসপি')
    I = 'Inspector', _('ইন্সপেক্টর')
    SI = 'SI', _('এসআই')
    ASI = 'ASI', _('এএসআই')
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
    I = 'Inspector', _('ইন্সপেক্টর')
    SI = 'SI', _('এসআই')
    ASI = 'ASI', _('এএসআই')
    NA = 'NA', _('প্রযোজ্য নহে')

# Create your models here.
class Police(models.Model):
    police_name_bangla = models.CharField(max_length=200, default='', verbose_name='নাম (বাংলা)')
    police_name_english = models.CharField(max_length=200, default='', verbose_name='নাম (ইংরেজি)')
    police_id = models.CharField(max_length=50, primary_key = True, verbose_name='পুলিশর আইডি নং')
    police_rank = models.CharField(max_length=10, choices=PoliceRanks.choices, default=PoliceRanks.NA, verbose_name='বর্তমান পদবী')
    police_designation = models.CharField(max_length=200, default='', blank=True, verbose_name='কর্মরত পদ')
    police_present = models.CharField(max_length=200, default='', blank=True, verbose_name='বর্তমান কর্মস্থল')

    police_father = models.CharField(max_length=200, default='', blank=True, verbose_name='পিতার নাম')
    police_mother = models.CharField(max_length=200, default='', blank=True, verbose_name='মাতার নাম')
    police_spouse = models.CharField(max_length=200, default='', blank=True, verbose_name='স্পাউস (স্বামী/স্ত্রী) এর নাম')
    police_gender = models.CharField(max_length=10, choices=Genders.choices, default=Genders.Male, verbose_name='লিঙ্গ')
    police_nid = models.CharField(max_length=200, default='', blank=True, verbose_name='জাতীয় আইডি নং')
    police_district = models.CharField(max_length=50, choices=Districts.choices, default=Districts.Comilla, verbose_name='নিজ জেলা')
    police_address_permanent = models.CharField(max_length=2000, blank=True, default='', verbose_name='স্থায়ী ঠিকানা')
    police_address_present = models.CharField(max_length=2000, blank=True, default='', verbose_name='বর্তমান ঠিকানা')
    police_dob = models.DateField(default=get_default_dob, verbose_name='জন্ম তারিখ')
    police_batch = models.CharField(max_length=5, choices=Batches.choices, default=Batches.ThirtySix, verbose_name='বিসিএস ব্যাচ')
    police_merit = models.CharField(max_length=5, default='', verbose_name='PSC Merit List')
    # 3 calculated fields here

    police_joining_rank = models.CharField(max_length=10, choices=JoiningRanks.choices, default=JoiningRanks.ASP, verbose_name='চাকুরীতে যোগদানের পদ')
    police_blood_group = models.CharField(max_length=10, choices=BloodGroups.choices, default=BloodGroups.Op, verbose_name='রক্তের গ্রুপ')
    police_religion = models.CharField(max_length=10, choices=Religions.choices, default=Religions.Islam, verbose_name='ধর্ম')
    police_mobile = models.CharField(max_length=200, default='', blank=True, verbose_name='ফোন নম্বর')
    police_email = models.CharField(max_length=200, default='', blank=True, verbose_name='ই-মেইল')
    police_promotion_date = models.DateField(default=get_default_my_date, verbose_name='বর্তমান পদে পদোন্নতির তারিখ')
    police_present_status = models.CharField(max_length=10, choices=PresentStatus.choices, default=PresentStatus.OnJob, verbose_name='বর্তমান অবস্থা')
    police_edu = models.CharField(max_length=200, default='', blank=True, verbose_name='শিক্ষাগত যোগ্যতা')
    
    police_past = models.CharField(max_length=2000, default='', blank=True, verbose_name='পূর্ববর্তী কর্মস্থল সমূহ')
    police_family_background = models.CharField(max_length=2000, default='', blank=True, verbose_name='পারিবারিক ইতিহাস')
    police_political_background = models.CharField(max_length=2000, default='', blank=True, verbose_name='রাজনৈতিক ইতিহাস')
    police_comments = models.CharField(max_length=1000, default='', blank=True, verbose_name='পর্যবেক্ষণ মন্তব্য')
    
    
    police_category = models.CharField(max_length=1, choices=[('A','A'), ('B','B'), ('C', 'C')], default='A')
    police_image = models.ImageField(upload_to = user_directory_path, default='logo.jpeg', verbose_name='ছবি')
    #police_image_url = models.CharField(max_length=1000, default='', blank=True, verbose_name='ছবি (S3)')
    
    
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