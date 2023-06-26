from random import choices

from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def rating_validator(value):
    if not 0.1 <= value <= 5.0:
        raise ValidationError("The rating must be between 0.1 and 5.0.")


# Create your models here.
class Profile(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(12)]
    )
    password = models.CharField(
        null=False,
        blank=False,
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
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('id',)


class Game(models.Model):
    GAME_CHOICES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        unique=True,
    )
    category = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        choices=GAME_CHOICES
    )
    rating = models.FloatField(
        null=False,
        blank=False,
        validators=[rating_validator]
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=[validators.MinValueValidator(1)]
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    summary = models.TextField(
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('id',)