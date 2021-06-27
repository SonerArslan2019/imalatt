from django import template

register = template.Library()


@register.filter
def mul(x, y):
    return x * y


@register.filter
def div_int(x, y):
    return round(x / y)
