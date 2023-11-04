from django.shortcuts import render
from django.http import HttpResponseServerError
from .forms import ConverterForm


def view_base_page(request):
    if request.method == 'POST':
        form = ConverterForm(request.POST)

        if form.is_valid():
            to_currency = request.POST['currency_to']
            from_currency = request.POST['currency_from']
            amount = request.POST['amount']

            result = round((float(to_currency) / float(from_currency)) * float(amount), 2)
            return render(request, 'index.html', {'form': form, 'result': result})
        else:
            return HttpResponseServerError('error500.html')
    else:
        form = ConverterForm()
        return render(request, 'index.html', {'form': form})
