import requests
import sys
from pprint import pformat

def get_country_data(country_code: str) -> dict:
    return requests.get(f"https://restcountries.eu/rest/v2/alpha/{country_code}")

if __name__ == "__main__":
    country_code = input("Bitten geben Sie einen Ländercode ein: ")

    if not country_code:
        sys.exit("Sie haben keinen Code eingegeben!")
    
    country_data = get_country_data("de")

    print(pformat(country_data.json()))
