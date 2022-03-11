import requests


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org"

    def __init__(self, APP_ID):
        self.APP_ID = APP_ID

    def _get_currencies(self):
        return requests.get(f"{self.BASE_URL}/currencies.json").json()

    @property
    def latest(self):
        return requests.get(f"{self.BASE_URL}/api/latest.json?app_id={self.APP_ID}").json()

    def convert(self, from_amount, from_currency, to_currency):
        rate = self.latest['rates']
        to_rate = rate[to_currency]

        if from_currency == 'USD':
            conv = from_amount * to_rate
            print(f"{from_amount} {from_currency}'s = {conv} {to_currency}'s")
        else:
            to_usd = from_amount / rate[from_currency]
            conv = to_usd * to_rate
            print(f"{from_amount} {from_currency}'s = {conv} {to_currency}'s")

    def default_rates(self, from_currency, to_currency):
        rate = self.latest['rates']
        to_rate = rate[to_currency]

        if from_currency == 'USD':
            print(f"1 {from_currency} = {to_rate} {to_currency}")

        else :
            from_base_def = 1/rate[from_currency]
            to_base_def = from_base_def * to_rate
            print(f"1 {from_currency} = {to_base_def} {to_currency}")

