from django.shortcuts import render
from .forms import ConverterForm


def view_base_page(request):
    form = ConverterForm({'amount_from': 0.0, 'amount_to': 0.0})
    return render(request, 'index.html', {'form': form})
