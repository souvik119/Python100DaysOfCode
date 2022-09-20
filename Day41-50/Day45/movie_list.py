from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, "html.parser")

movie_titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

#reversing the list to write to the file from 1 to 100
movie_titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")