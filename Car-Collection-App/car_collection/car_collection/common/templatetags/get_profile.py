from django import template

from car_collection.profile_car.models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile():
    return Profile.objects.first()
