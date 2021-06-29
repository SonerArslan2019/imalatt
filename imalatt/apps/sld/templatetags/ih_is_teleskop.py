from django import template

register = template.Library()


@register.filter
def gecis_genisligi_hesaplama(gecis_genisligi):
    return kanat_genisligi_hesaplama(gecis_genisligi) - 84


@register.filter
def kanat_genisligi_hesaplama(gecis_genisligi):
    return round((gecis_genisligi + 42) / 2)


@register.filter
def etek_olcusu(gecis_genisligi):
    return kanat_genisligi_hesaplama(gecis_genisligi) - 48
