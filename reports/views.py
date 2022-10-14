from .models import Police
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from wkhtmltopdf.views import PDFTemplateView
from django.views.generic import TemplateView
import bangla
from django.core.files.storage import get_storage_class

replace_map = {
    'year': 'বছর',
    'month': 'মাস',
    'day': 'দিন',
    'On Job':'চাকুরীরত',
    'Sacked':'চাকুরীচ্যুত',
    'Retired':'অবসরপ্রাপ্ত',
    'ASP':'এএসপি',
    'SP':'এসপি',
    'Inspector':'ইন্সপেক্টর',
    'ASI':'এএসআই',
    'SI':'এসআই',
    'IGP':'আইজিপি',
    'DIG':'ডিআইজি',
    'IG':'আইজি',
    'Addl.': 'অতিঃ',
    'Sr. ': 'সিনিয়র',
    'NA':'প্রযোজ্য নহে',
    'Male':'পুরুষ',
    'Female':'মহিলা',
    'Islam':'ইসলাম',
    'Hindu':'হিন্দু',
    'Christian':'খ্রিস্টান',
    'Buddha':'বৌদ্ধ',
    'Others':'অন্যান্য'
}

def get_joining_date_from_batch(batch):
    match batch:
        case '7': return datetime(1988, 2, 15)
        case '8': return datetime(1989, 12, 20)
        case '12': return datetime(1991, 1, 20)
        case '15': return datetime(1995, 11, 15)
        case '17': return datetime(1998, 2, 22)
        case '18': return datetime(1999, 1, 25)
        case '20': return datetime(2001, 5, 31)
        case '21': return datetime(2003, 5, 10)
        case '22': return datetime(2003, 12, 10)
        case '24': return datetime(2005, 7, 2)
        case '25': return datetime(2006, 8, 21)
        case '27': return datetime(2008, 11, 13)
        case '28': return datetime(2010, 12, 1)
        case '29': return datetime(2011, 8, 1)
        case '30': return datetime(2012, 6, 3)
        case '31': return datetime(2013, 1, 15)
        case '33': return datetime(2014, 8, 7)
        case '34': return datetime(2016, 6, 1)
        case '35': return datetime(2017, 5, 2)
        case '36': return datetime(2018, 9, 3)
        case _: return datetime(2099, 12, 31)
def get_resigning_date_from_dob(dob):
    return dob.replace(year=dob.year + 59)
def get_expiry_from_dob(dob):
    resigning_date = get_resigning_date_from_dob(dob)
    rdelta = relativedelta(resigning_date, date.today())
    return rdelta

def stringify_date(date):
    return date.strftime('%d/%m/%Y')
def stringify_duration(duration):
    return "{} year {} month {} day".format(duration.years, duration.months, duration.days)

def begalize(string):
    string = str(string)
    for word, initial in replace_map.items():
        string = string.replace(word, initial)
    return bangla.convert_english_digit_to_bangla_digit(string)

class MyPDF(PDFTemplateView):
    filename = 'pdf.pdf'
    template_name = 'pdf.html'
    model = Police
    cmd_options = {
        'margin-top': 3
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        police_id = self.kwargs['police_id']
        police = Police.objects.get(pk=police_id)
        police_dob = getattr(police, 'police_dob')
        police_batch = getattr(police, 'police_batch')
        police_image = getattr(police, 'police_image')
        
        fields = []
        for field in Police._meta.get_fields():
            if field.name == 'police_dob':
                fields.append({
                    'name': field.name,
                    'verbose_name': field.verbose_name,
                    'value': begalize(stringify_date(police_dob))
                })
            elif field.name in ['police_batch', 'police_religion', 'police_rank', 'police_joining_rank', 'police_present_status', 'police_gender']:
                fields.append({
                    'name': field.name,
                    'verbose_name': field.verbose_name,
                    'value': begalize(getattr(police, field.name))
                })
            elif field.name in ['police_designation', 'police_political_background']:
                value = getattr(police, field.name)
                value = 'প্রযোজ্য নহে' if value == '' else value
                fields.append({
                    'name': field.name,
                    'verbose_name': field.verbose_name,
                    'value': value
                })
            elif field.name == 'police_merit':
                joining_date = get_joining_date_from_batch(police_batch)
                resigning_date = get_resigning_date_from_dob(police_dob)
                expiry = get_expiry_from_dob(police_dob)
                fields.append({
                    'name': 'joining_date',
                    'verbose_name': 'চাকুরীতে যোগদানের তারিখ',
                    'value': begalize(stringify_date(joining_date))
                })
                fields.append({
                    'name': 'resigning_date',
                    'verbose_name': 'স্বাভাবিক অবসর গ্রহণের তারিখ',
                    'value': begalize(stringify_date(resigning_date))
                })
                fields.append({
                    'name': 'expiry',
                    'verbose_name': 'চাকুরীর অবশিষ্ট মেয়াদ',
                    'value': begalize(stringify_duration(expiry))
                })
            else:
                fields.append({
                    'name': field.name,
                    'verbose_name': field.verbose_name,
                    'value': getattr(police, field.name)
                })
        context['fields'] = fields
        context['id'] = police_id
        context['image'] = get_storage_class()().url(name=police_image.name)
        
        return context