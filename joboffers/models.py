import uuid as uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class JobOffer(models.Model):
    class Experience(models.TextChoices):
        NO_EXPERIENCE = 'No experience'
        JUNIOR = 'About 1 year experience'
        MID_EXPERIENCE = 'From 1 to 3 years experience'
        SENIOR = 'From 3 to 5 years experience'
        EXPERT = 'More than 5 years experience'

    class Status(models.TextChoices):
        DRAFT = 'Draft',
        PUBLISHED = 'Published'
        DELETED = 'Deleted'

    # ID
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # Foreign Keys
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, )
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    location = models.ForeignKey('City', on_delete=models.PROTECT)

    # Own models
    title = models.CharField(max_length=256, default='No title')
    speciality = models.CharField(max_length=140, default='No speciality')
    description = models.TextField(max_length=1000, default='No description')
    required_experience = models.CharField(max_length=50,
                                           choices=Experience.choices,
                                           default=Experience.NO_EXPERIENCE
                                           )

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    publication_status = models.CharField(max_length=10,
                                          choices=Status.choices,
                                          default=Status.DRAFT)

    salary = models.IntegerField(blank=False)

    slug = models.SlugField(max_length=250, unique_for_date='publish')

    company_in_secret = models.BooleanField(
        default=False,
        help_text="Whether to maintain the company's name secret"
    )

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title



class Company(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=140, default='Unknown')
    description = models.TextField(max_length=500, default='No description')
    webpage = models.URLField(max_length=256, default='')


class City(models.Model):

    class TimeZones(models.TextChoices):
        EASTERN = "Eastern"
        CENTRAL = "Central"
        MOUNTAIN = "Mountain"
        PACIFIC = "Pacific"
        ALASKA = "Alaskan"
        HAWAII = "Hawaii"

    name = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=50)
    timezone = models.CharField(max_length=10,
                                choices=TimeZones.choices)
