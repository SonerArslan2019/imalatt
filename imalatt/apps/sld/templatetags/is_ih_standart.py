from django import template

register = template.Library()


@register.filter
def gecis_genisligi_hesaplama(toplam_genislik):
    return round(toplam_genislik / 2) - 42


@register.filter
def kanat_genisligi_hesaplama(toplam_genislik):
    return round((gecis_genisligi_hesaplama(toplam_genislik) + 84) / 2)
