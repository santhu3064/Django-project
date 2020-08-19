from django import template

register = template.Library()


@register.filter(name='parents')
def parents(value):
    if 'lakshmi' in value.lower():
        return 'Mom'
    else:
        return "Mummy"
