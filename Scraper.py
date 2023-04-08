import csv
from bs4 import BeautifulSoup
import requests


def scraper():
    url = "http://books.toscrape.com/"
    request_url = requests.get(url)
    initial_soup = BeautifulSoup(request_url.content, "html.parser")
    soupify = initial_soup.find_all(class_="nav nav-list")

    for soup in soupify:
        href_tag = soup.find_all('a')
        for ag in href_tag:
            print(ag['href'])


scraper()