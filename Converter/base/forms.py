from django import forms
from .rates import get_rates


class ConverterForm(forms.Form):
    amount = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': '0.001'}))
    currency_from = forms.ChoiceField(choices=get_rates(), widget=forms.Select(attrs={'class': 'form-select'}))
    currency_to = forms.ChoiceField(choices=get_rates(), widget=forms.Select(attrs={'class': 'form-select'}))
