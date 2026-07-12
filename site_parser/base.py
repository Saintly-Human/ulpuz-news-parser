from settings import BASE_URL
import requests
from bs4 import BeautifulSoup


class BaseParser:
    @staticmethod
    def get_soup(url=BASE_URL):
        html = requests.get(url).text
        return BeautifulSoup(html, 'html.parser')