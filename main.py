import requests
from tabulate import tabulate


class CountriesInfo:
    def __init__(self):
        self.api_url = 'https://restcountries.com/v3.1/all'

    def fetch_data(self) -> dict:
        response = requests.get(url=self.api_url, headers={'accept': 'application/json'})
        if response.status_code == 200:
            return response.json()

    def display_data(self) -> None:
        data = self.fetch_data()
        headers = ['Country Name', 'Capital', 'Flag']
        table_data = []

        if data is None:
            raise Exception('Data not found')

        for country in data:
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', 'N/A')
            capital = capital[0] if (type(capital) is list and len(capital) == 1) else capital
            flag = country.get('flags', {}).get('png', 'N/A')
            table_data.append([name, capital, flag])

        table = tabulate(table_data, headers=headers, tablefmt='plain')
        print(table)
        

if __name__ == '__main__':
    countries = CountriesInfo()
    countries.display_data()
