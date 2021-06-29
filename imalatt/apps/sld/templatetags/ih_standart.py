from django import template

register = template.Library()

@register.filter
def kanat_genisligi_hesaplama(gecis_genisligi):
    return round((gecis_genisligi + 84) / 2)
