from django import forms
from .rates import get_rates


class ConverterForm(forms.Form):
    rates_data = get_rates()

    amount_from = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'type': 'number',
                                                                 'step': '0.001',
                                                                 'id': 'input_form'}))
    amount_to = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'type': 'number',
                                                               'step': '0.001',
                                                               'id': 'output_form'}))
    currency_from = forms.ChoiceField(choices=rates_data, widget=forms.Select(attrs={'class': 'form-select',
                                                                                      'id': 'curr_from'}))
    currency_to = forms.ChoiceField(choices=rates_data, widget=forms.Select(attrs={'class': 'form-select',
                                                                                    'id': 'curr_to'}))
