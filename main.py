import requests
import typer

from bs4 import BeautifulSoup


def main(country: str):
    url = 'https://world-weather.ru/pogoda/russia/{country}/'.format(country=country)
    res = requests.get(url)
    html_doc = res.text


    soup = BeautifulSoup(html_doc, 'html.parser')

    tag = soup.find(id="weather-now-number")

    current_wheather = tag.contents[0]

    print(f"Current wheather in {country}: {current_wheather}")

if __name__ == "__main__":
    typer.run(main)


