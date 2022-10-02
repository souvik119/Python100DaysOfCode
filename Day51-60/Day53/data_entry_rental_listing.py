import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ZILLOW_URL = "https://www.zillow.com/mira-mesa-san-diego-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A32.951278668974716%2C%22east%22%3A-117.08861565635414%2C%22south%22%3A32.88297412722187%2C%22west%22%3A-117.17959618613929%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A587533%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A116625%2C%22regionType%22%3A8%7D%5D%7D"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfXrYOxma1QLS1QoI3qjH3WDeHcF83p4hxYgRq9tJiiUz_sNw/viewform?usp=sf_link"
CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
header = {
        "User-Agent": "Defined",
        "Accept-Language": "en-US,en;q=0.5"
}


response = requests.get(ZILLOW_URL, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

#getting links
link_elements = [link["href"] for link in soup.select(".property-card-link")]
#some links do not have the starting https:....
links = []
for link in link_elements:
    if "https" not in link:
        new_link = "https://www.zillow.com" + link
        if new_link not in links:
            links.append(new_link)
    else:
        if link not in links:
            links.append(link)


#getting addresses
addresses = [address.getText().split(" | ")[-1] for address in soup.select(".property-card-link address")]


#getting rent
rent_elements = [rent.getText() for rent in soup.select(".kJFQQX span")]
rents = []
for rent in rent_elements:
    if "+" in rent:
        rents.append(rent.split("+")[0])
    elif "/" in rent:
        rents.append(rent.split("/")[0])


#filling in form
s = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=s)

for n in range(len(rents)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(addresses[n])
    rent.send_keys(rents[n])
    link.send_keys(links[n])
    submit.click()
