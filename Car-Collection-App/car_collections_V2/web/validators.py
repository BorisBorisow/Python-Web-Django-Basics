from django.core.exceptions import ValidationError


def min_length_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def year_validator(value):
    if not 1980 <= value <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')

