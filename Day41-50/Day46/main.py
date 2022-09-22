from urllib import response
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100/"

def get_full_url():
    user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    return BILLBOARD_BASE_URL + user_date + "/", user_date


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    song_names = [name.getText().strip() for name in soup.select(selector="li h3", class_="c-title")]
    song_titles = song_names[0:100]
    return song_titles

def spotify(song_titles):
    sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]
    print(user_id)
    song_uris = []
    year = date.split("-")[0]
    for song in song_titles:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    #Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    print(playlist)

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)



def main():
    user_date, date = get_full_url()
    song_title = scrape_data(user_date)
    spotify(song_title, date)

main()