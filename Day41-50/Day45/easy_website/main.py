from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

#get title
print(soup.title)

#get title name
print(soup.title.string)

#get entire website
# print(soup.prettify())

#get first a tag
print(soup.a)

#get all a tags
print(soup.find_all(name="a"))

#get all p tags text within p tags
all_p_tags = soup.find_all(name="p")

for tag in all_p_tags:
    print(tag.getText())


#get the actual href in a tags
for tag in soup.find_all(name="a"):
    print(tag.get("href"))


#get by name of id
heading = soup.find(name="h1", id="name")
print(heading.getText())

#for class use class_=

#using css selector
company_url = soup.select_one(selector="p a")
print()