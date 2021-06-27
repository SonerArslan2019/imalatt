from django.db import models

from ckeditor.fields import RichTextField

from .variables import DELIVERY_TYPES, COLORS, GLASS_TYPES


class WorkOrderAbstractModel(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    crm = models.CharField('CRM NO', max_length=10)
    company_name = models.CharField(verbose_name='Firma', max_length=150)
    billing_address = models.CharField('Fatura Adresi', max_length=80)
    delivery_address = models.CharField('Sevk Adresi', max_length=80)
    delivery_date = models.DateField('Teslim Tarihi')
    created_time = models.DateTimeField('Oluşturma Tarihi', auto_now_add=True)
    delivery_type = models.CharField('Teslim Şekli', choices=DELIVERY_TYPES, max_length=10)
    has_chest = models.BooleanField('Sandıklı Mı?')

    glass = models.CharField('Cam',choices=GLASS_TYPES, max_length=25)
    color = models.CharField('Renk', max_length=20, choices=COLORS)
    notes = RichTextField('Notlar', blank=True, null=True)

    drawing = models.CharField('Hazırlayan', max_length=200)
    control = models.CharField('Kontrol', blank=True, null=True, max_length=40)
    manufacturing_chief = models.CharField('İmalat Şefi', blank=True, null=True, max_length=40)


    def __str__(self):
        return f'{self.crm} {self.company_name}'

    class Meta:
        abstract = True