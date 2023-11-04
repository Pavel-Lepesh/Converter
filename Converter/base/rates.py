import requests


def get_rates():
    response = requests.get(url='https://v6.exchangerate-api.com/v6/1b90527463b7996bd1752453/latest/USD').json()
    rates = tuple((value, currency) for currency, value in response['conversion_rates'].items())
    print('!!!')
    return rates
