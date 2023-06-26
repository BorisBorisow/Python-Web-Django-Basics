from django.core.exceptions import ValidationError


def capital_letter_checker(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def only_letters_checker(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')
