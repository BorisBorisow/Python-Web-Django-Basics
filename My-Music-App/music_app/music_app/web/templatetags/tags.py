from django import template

from music_app.web.models import Profile

register = template.Library()


@register.inclusion_tag(
    'tags/navigation.html',
    name='custom_navigation'
)
def inclusion_custom_navigation():
    inner_context = {
        "profile": Profile.objects.first()
    }
    return inner_context
