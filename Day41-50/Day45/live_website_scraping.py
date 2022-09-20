from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# get article title, link and upvotes
# article_tag = soup.find(name="a", class_="titlelink")
# article_title = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_title, article_link, article_upvote)

# repeating the same for all the links on page

article_texts = []
article_links = []

for article_tag in soup.find_all(name="a", class_="titlelink"):
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# getting most upvoted article
largest_upvote = max(article_upvotes)
largest_index = article_upvotes.index(largest_upvote)

print(article_texts[largest_index], article_links[largest_index])