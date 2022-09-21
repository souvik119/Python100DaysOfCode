from urllib import response
import requests
from bs4 import BeautifulSoup

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100/"

def get_full_url():
    user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    return BILLBOARD_BASE_URL + user_date + "/"


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names = [name.getText().strip() for name in soup.select(selector="li h3", class_="c-title")]
    song_titles = song_names[0:100]
    print(song_titles)



def main():
    user_date = get_full_url()
    scrape_data(user_date)


main()