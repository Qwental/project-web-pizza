from django import template
from users.utils import show_notification

register = template.Library()


@register.simple_tag()
def get_notifications(user):
    return show_notification(user)
