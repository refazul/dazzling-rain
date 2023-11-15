from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Spouse(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='spouse', null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Person.GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Child(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='child', null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Person.GENDER_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Address(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='address', null=True)
    house_no = models.CharField(max_length=100)
    road_no = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    thana = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.house_no}, Road {self.road_no}, {self.area}, {self.thana}, {self.district}, {self.division}, {self.postal_code}"

class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='educational_qualifications', null=True)
    institution_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution_name}"

class Posting(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='posting_records', null=True)
    designation = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    pay_scale = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.designation} at {self.organization}, {self.location}"

class ServiceHistory(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='service_history', null=True)
    govt_service_date = models.DateField()
    gazetted_date = models.DateField(null=True, blank=True)
    encadrement_date = models.DateField(null=True, blank=True)
    cadre = models.CharField(max_length=100)

    def __str__(self):
        return f"Cadre: {self.cadre}, Govt. Service Start: {self.govt_service_date.strftime('%Y-%m-%d')}"

class LocalTraining(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='local_trainings', null=True)
    course_title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    duration = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # in days

    def __str__(self):
        return f"{self.course_title} at {self.institution}"