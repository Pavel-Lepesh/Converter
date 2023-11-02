from django.shortcuts import render
import requests


def view_base_page(request):
    response = requests.get(url='https://v6.exchangerate-api.com/v6/1b90527463b7996bd1752453/latest/USD').json()
    rates: dict = response['conversion_rates']
    if request.method == 'POST':
        from_currency = request.POST['select_from']
        to_currency = request.POST['select_to']
        amount = request.POST['amount']

        result = round((rates[to_currency] / rates[from_currency]) * float(amount), 2)

        context = {
            'rates': rates,
            'result': result,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount
        }
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'index.html', {'rates': rates.keys()})
