from django import template
from django.template.defaulttags import register

@register.simple_tag(takes_context=True)
def set_var(context, name, value):
    context[name] = value
    return ''
