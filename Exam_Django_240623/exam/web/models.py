from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def name_min_length_validator(value):
    if len(value) < 2:
        raise ValidationError("Name length must be minimum 2 characters")


def name_start_with_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


def name_contain_only_letter_validator(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


class Profile(models.Model):
    MAX_LENGTH_FIRST_NAME = 25
    MIN_LENGTH_FIRST_NAME = 2

    MAX_LENGTH_LAST_NAME = 35
    MIN_LENGTH_LAST_NAME = 1

    MAX_LENGTH_EMAIL = 40
    MIN_LENGTH_PASSWORD = 8
    DEFAULT_AGE_VALUE = 18

    MAX_LENGTH_PASSWORD = 20

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        blank=False,
        null=False,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            name_start_with_letter_validator,
        ]

    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        blank=False,
        null=False,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            name_start_with_letter_validator,
        ]
    )
    email = models.EmailField(
        blank=False,
        null=False,
        max_length=MAX_LENGTH_EMAIL
    )
    password = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LENGTH_PASSWORD,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_PASSWORD),
        ]
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=DEFAULT_AGE_VALUE
    )


class Fruit(models.Model):
    MAX_LENGTH_NAME = 30
    MIN_LENGTH_NAME = 2

    name = models.CharField(
        blank=False,
        null=False,
        max_length=MAX_LENGTH_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_NAME),
            name_contain_only_letter_validator
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
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
