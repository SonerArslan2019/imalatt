from django import template

register = template.Library()


@register.simple_tag
def calculate(*args):
    return str(eval(expression))
