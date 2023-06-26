from django.core import validators
from django.db import models


# Create your models here.

class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[validators.MinLengthValidator(
            2,
            "The username must be a minimum of 2 chars"
        )],
        null=False,
        blank=False
    )

    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(18)],
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
        null=True,
        blank=True,
    )

    def get_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ''
