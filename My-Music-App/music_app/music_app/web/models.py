from django.core import validators
from django.db import models

from music_app.web.validators import alphanumeric_and_underscore_validator, float_positive_validator


# Create your models here.
class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(2),
            alphanumeric_and_underscore_validator,
        ]
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

class Album(models.Model):
    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other")
    ]

    album_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )
    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=GENRE_CHOICES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[float_positive_validator]
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
