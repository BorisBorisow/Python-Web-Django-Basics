from random import choices

from django.core import validators
from django.db import models

from web.validators import min_length_validator, year_validator


# Create your models here.


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[min_length_validator],
        null=False,
        blank=False,

    )
    email = models.EmailField(
        null=True,
        blank=True,

    )
    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[validators.MinValueValidator(18)],
    )
    password = models.CharField(
        null=True,
        blank=True,
        max_length=30,

    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    CHOICES = (
        ("Sports car", "Sports car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )
    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=CHOICES,
    )
    model = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(2)],
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[year_validator]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(1)]
    )