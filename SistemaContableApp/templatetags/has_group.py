from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_names):
    group_names = group_names.split(',')
    return bool(user.groups.filter(name__in=group_names))