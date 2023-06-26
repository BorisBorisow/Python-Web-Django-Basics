from random import choices

from django.core import validators
from django.db import models

from my_plant_app.plants.validators import capital_letter_checker, only_letters_checker


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[validators.MinLengthValidator(2)],
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[capital_letter_checker]
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[capital_letter_checker]
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Plant(models.Model):
    CHOICES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),

    )
    plant_type = models.CharField(
        blank=False,
        null=False,
        max_length=14,
        choices=CHOICES,
    )
    name = models.CharField(
        blank=False,
        null=False,
        max_length=20,
        validators=[
            validators.MinLengthValidator(2),
            only_letters_checker
        ]
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[validators.MinValueValidator(1)]
    )

