from django.core import validators
from django.db import models

from car_collection.car.validators import years_validator


# Create your models here.
class Car(models.Model):
    CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other')
    )
    type = models.CharField(
        null=False,
        blank=False,
        choices=CHOICES,
        max_length=10,
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[validators.MinLengthValidator(2, "It should consist of a minimum of 2 characters.")],
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[years_validator]
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(1, "Price cannot be below 1.")]
    )
