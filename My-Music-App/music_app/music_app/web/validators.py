from django.core import exceptions


def alphanumeric_and_underscore_validator(value):
    for ch in value:
        if not ch.isalnum() and ch != "_":
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')

def float_positive_validator(value):
    if value < 0.0:
        raise exceptions.ValidationError('Ensure this value is greater than or equal to 0.0.')