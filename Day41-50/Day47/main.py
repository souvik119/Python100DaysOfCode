import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/Cricnix-Cricket-Elite-Practice-Training/dp/B08QHPBLRV/"
headers = {
        "User-Agent": "Defined",
        "Accept-Language": "en-US,en;q=0.5"
}

def scrape_price():
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    print(soup)

if __name__ == "__main__":
    scrape_price()
