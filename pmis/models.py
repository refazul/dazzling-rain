from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    YES_NO = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    TRAIN_TYPE = [
        ('LM', 'LOCAL (MANDATORY)'),
        ('L', 'LOCAL'),
        ('F', 'FOREIGN')
    ]

    person_name     = models.CharField(max_length=100, blank=True)
    name_bangla     = models.CharField(max_length=100, blank=True)
    father_name     = models.CharField(max_length=100, blank=True)
    mother_name     = models.CharField(max_length=100, blank=True)

    gender          = models.CharField(max_length=1, choices=GENDER_CHOICES)
    freedom_fighter = models.CharField(max_length=1, choices=YES_NO)

    date_of_birth           = models.DateField(null=True, blank=True)
    lpr_prl_date            = models.DateField(null=True, blank=True)
    order_date              = models.DateField(null=True, blank=True)
    join_date               = models.DateField(null=True, blank=True)
    cadre_date              = models.DateField(null=True, blank=True)
    confirmation_g_o_date   = models.DateField(null=True, blank=True)

    govt_id             = models.CharField(max_length=100, blank=True)
    rank                = models.CharField(max_length=100, blank=True)
    home_district       = models.CharField(max_length=100, blank=True)
    designation         = models.CharField(max_length=100, blank=True)
    organisation        = models.CharField(max_length=100, blank=True)
    cadre               = models.CharField(max_length=100, blank=True)
    batch               = models.CharField(max_length=100, blank=True)
    religion            = models.CharField(max_length=100, blank=True)
    marital_stat        = models.CharField(max_length=100, blank=True)
    nid                 = models.CharField(max_length=100, blank=True)
    mobile              = models.CharField(max_length=100, blank=True)
    email               = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.person_name} {self.name_bangla}"

class Spouse(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='spouse', null=True, default=None)

    spouse_name     = models.CharField(max_length=100, blank=True)
    occupation      = models.CharField(max_length=100, blank=True)
    designation     = models.CharField(max_length=100, blank=True)
    home_district   = models.CharField(max_length=100, blank=True)
    organisation    = models.CharField(max_length=100, blank=True)
    location        = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.spouse_name}"

class Address(models.Model):
    person                      = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='address', null=True, default=None)

    village_or_house_or_road    = models.CharField(max_length=100, blank=True)
    post_office                 = models.CharField(max_length=100, blank=True)
    police_station              = models.CharField(max_length=100, blank=True)
    district                    = models.CharField(max_length=100, blank=True)
    telephone_no                = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.district}"

class Child(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='child', null=True, default=None)

    child_name      = models.CharField(max_length=100, blank=True)
    date_of_birth   = models.DateField(null=True, blank=True)
    gender          = models.CharField(max_length=1, choices=Person.GENDER_CHOICES)

    def __str__(self):
        return f"{self.child_name}"

class Language(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='language', null=True, default=None)

    language_name   = models.CharField(max_length=10, blank=True)
    read            = models.CharField(max_length=1, choices=Person.YES_NO)
    write           = models.CharField(max_length=1, choices=Person.YES_NO)
    speak           = models.CharField(max_length=1, choices=Person.YES_NO)

    def __str__(self):
        return f"{self.language_name}"
class Education(models.Model):
    person              = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='education', null=True, default=None)

    name_of_institution = models.CharField(max_length=255, blank=True)
    principal_subject   = models.CharField(max_length=100, blank=True)
    degree              = models.CharField(max_length=100, blank=True)
    passing_year        = models.CharField(max_length=100, blank=True)
    result              = models.CharField(max_length=100, blank=True)
    gpa_or_cgpa         = models.CharField(max_length=100, blank=True)
    distinction         = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.degree}"

class Training(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='training', null=True, default=None)

    training_type   = models.CharField(max_length=50, choices=Person.TRAIN_TYPE)
    course_title    = models.CharField(max_length=255, blank=True)
    institution     = models.CharField(max_length=100, blank=True)
    position        = models.CharField(max_length=100, blank=True)

    from_date       = models.DateField(null=True, blank=True)
    to_date         = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.training_type}"

class Travel(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='travel', null=True, default=None)

    country         = models.CharField(max_length=255, blank=True)
    purpose         = models.CharField(max_length=100, blank=True)

    from_date       = models.DateField(null=True, blank=True)
    to_date         = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.country}"
class Abroad(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='abroad', null=True, default=None)

    post            = models.CharField(max_length=255, blank=True)
    organisation    = models.CharField(max_length=100, blank=True)
    country         = models.CharField(max_length=100, blank=True)

    from_date       = models.DateField(null=True, blank=True)
    to_date         = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.post}"

class Qualification(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='qualification', null=True, default=None)

    qualification   = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f"{self.qualification}"



class Publication(models.Model):
    person                  = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='publication', null=True, default=None)

    book                    = models.CharField(max_length=255, blank=True)
    periodical_monograph    = models.CharField(max_length=255, blank=True)
    journals                = models.CharField(max_length=255, blank=True)
    description             = models.CharField(max_length=255, blank=True)

    date                    = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.book}"



class Honour(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='honour', null=True, default=None)

    title_of_award  = models.CharField(max_length=255, blank=True)
    ground          = models.CharField(max_length=255, blank=True)

    date            = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.title_of_award}"

class Other(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='other', null=True, default=None)

    name_of_employeer   = models.CharField(max_length=255, blank=True)
    address             = models.CharField(max_length=255, blank=True)
    type_of_service     = models.CharField(max_length=255, blank=True)
    posting             = models.CharField(max_length=255, blank=True)

    from_date           = models.DateField(null=True, blank=True)
    to_date             = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.name_of_employeer}"



class Service(models.Model):
    person              = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='service', null=True, default=None)

    cadre = models.CharField(max_length=100, blank=True)

    govt_service_date   = models.DateField(null=True, blank=True)
    gazetted_date       = models.DateField(null=True, blank=True)
    encadrement_date    = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"Cadre: {self.cadre}"

class Promotion(models.Model):
    person              = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='promotion', null=True, default=None)
    rank                = models.CharField(max_length=100, blank=True)
    nature_of_promotion = models.CharField(max_length=100, blank=True)
    pay_scale           = models.CharField(max_length=100, blank=True)

    promotion_date      = models.DateField(null=True, blank=True)
    g_o_date            = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Cadre: {self.rank}"


class Prosecution(models.Model):
    person              = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='prosecution', null=True, default=None)
    nature_of_offence   = models.CharField(max_length=100, blank=True)
    punishment          = models.CharField(max_length=100, blank=True)
    remarks             = models.CharField(max_length=100, blank=True)

    date                = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Cadre: {self.nature_of_offence}"

class Posting(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='posting', null=True, default=None)
    designation     = models.CharField(max_length=100, blank=True)
    organisation    = models.CharField(max_length=100, blank=True)
    location        = models.CharField(max_length=100, blank=True)
    pay_scale       = models.CharField(max_length=100, blank=True)

    from_date       = models.DateField(null=True, blank=True)
    to_date         = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Cadre: {self.designation}"