from django import forms

from bootstrap_datepicker_plus import DatePickerInput

from .models import SLD


class SLDForm(forms.ModelForm):
    class Meta:
        model = SLD
        fields = [
            'crm',
            'company_name',
            'billing_address',
            'delivery_address',
            'delivery_date',
            'delivery_type',
            'has_chest',
            'glass',
            'color',
            'notes',
            'drawing',
            'control',
            'manufacturing_chief',
            'door_type',
            'pass_width',
            'pass_height',
            'ustluk',
            'total_width',
            'total_height',
            'mechanism_width',
            'opening_direction',
            'options',
            'radar_activations',
        ]
        widgets = {
            'delivery_date': DatePickerInput(format='%d/%m/%Y'),
        }