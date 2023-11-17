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
    organization        = models.CharField(max_length=100, blank=True)
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
    person      = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='spouse', null=True, default=None)
    spouse_name = models.CharField(max_length=100, blank=True)
    gender      = models.CharField(max_length=1, choices=Person.GENDER_CHOICES)

    def __str__(self):
        return f"{self.spouse_name}"

class Child(models.Model):
    person      = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='child', null=True, default=None)
    child_name  = models.CharField(max_length=100, blank=True)
    gender      = models.CharField(max_length=1, choices=Person.GENDER_CHOICES)

    def __str__(self):
        return f"{self.child_name}"

class Address(models.Model):
    person      = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='address', null=True, default=None)
    house_no    = models.CharField(max_length=100, blank=True)
    road_no     = models.CharField(max_length=100, blank=True)
    area        = models.CharField(max_length=100, blank=True)
    thana       = models.CharField(max_length=100, blank=True)
    district    = models.CharField(max_length=100, blank=True)
    division    = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.house_no}, Road {self.road_no}, {self.area}, {self.thana}, {self.district}, {self.division}, {self.postal_code}"

class Education(models.Model):
    person              = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='educational_qualifications', null=True, default=None)
    institution_name    = models.CharField(max_length=255, blank=True)
    degree              = models.CharField(max_length=100, blank=True)
    field_of_study      = models.CharField(max_length=100, blank=True)
    start_year          = models.CharField(max_length=100, blank=True)
    end_year            = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution_name}"

class Posting(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='posting_records', null=True, default=None)
    designation     = models.CharField(max_length=100, blank=True)
    organization    = models.CharField(max_length=100, blank=True)
    location        = models.CharField(max_length=100, blank=True)
    from_date       = models.DateField(null=True, blank=True)
    to_date         = models.DateField(null=True, blank=True)
    pay_scale       = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.designation} at {self.organization}, {self.location}"

class ServiceHistory(models.Model):
    person              = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='service_history', null=True, default=None)
    govt_service_date   = models.DateField(null=True, blank=True)
    gazetted_date       = models.DateField(null=True, blank=True)
    encadrement_date    = models.DateField(null=True, blank=True)
    cadre               = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Cadre: {self.cadre}"

class LocalTraining(models.Model):
    person          = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='local_trainings', null=True, default=None)
    course_title    = models.CharField(max_length=255, blank=True)
    institution     = models.CharField(max_length=255, blank=True)
    position        = models.CharField(max_length=100, blank=True)
    from_date       = models.DateField(null=True, blank=True)
    to_date         = models.DateField(null=True, blank=True)
    duration        = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.course_title} at {self.institution}"