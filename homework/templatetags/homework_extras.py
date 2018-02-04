import re

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def active_url(context, url, message='active'):
    try:
        pattern = '^%s$' % reverse(url)
    except NoReverseMatch:
        pattern = url

    path = context['request'].path
    return message if re.search(pattern, path) else ''
