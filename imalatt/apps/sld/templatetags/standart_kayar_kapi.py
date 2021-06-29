from django import template

register = template.Library()


@register.simple_tag
def calculate(*args):
    expression = ''.join(str(i) for i in args)
    return str(eval(expression))


@register.simple_tag
def ray_kapak_kapak_olcusu(gecis_genisligi):
    return (2 * (gecis_genisligi + 84)) + 8
