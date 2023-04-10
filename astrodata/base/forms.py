from django.forms import FloatField, Form, TypedChoiceField
from django.forms.widgets import NumberInput, Select
from django.utils.html import format_html

MODE_TYPES = (
    ('CIE', 'Collisional Ionisation Equilibrium (CIE)'),
    ('PIE', 'Photoionization Equilibrium (PIE)'),
)


class InterpolateForm(Form):
    nH = FloatField(required=True,
                    label=format_html('Number Density of Hydrogen (cm<sup>-3</sup>)'),
                    widget=NumberInput(attrs={'class': 'form-control'}))

    mode = TypedChoiceField(choices=MODE_TYPES,
                            required=True,
                            initial=MODE_TYPES[0],
                            label='Select Mode',
                            widget=Select(attrs={'class': 'form-select'}))

    temperature = FloatField(required=True,
                             label='Temperature (in Kelvins)',
                             widget=NumberInput(attrs={'class': 'form-control'}))

    metallicity = FloatField(required=True,
                             label=format_html('Metallicity (Z<sub>&#8857;</sub>)'),
                             widget=NumberInput(attrs={'class': 'form-control'}))

    redshift = FloatField(required=True,
                          label='Cosmic Redshift',
                          widget=NumberInput(attrs={'class': 'form-control'}))
