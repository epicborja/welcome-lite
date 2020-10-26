from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    class UserType(models.TextChoices):
        EMPLOYER = 'Employer'
        EMPLOYEE = 'Employee'

    class PremiumPlan(models.TextChoices):
        FREE = 'Free',
        PREMIUM = 'Premium',
        BUSINESS = 'Business',
        NO_PLAN = ''

    user_type = models.CharField(
        max_length = 8,
        choices = UserType.choices,
        default = UserType.EMPLOYER
    )

    plan = models.CharField(
        max_length=10,
        choices=PremiumPlan.choices,
        default=PremiumPlan.NO_PLAN
    )

