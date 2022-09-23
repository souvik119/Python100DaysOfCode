from unicodedata import name
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

SMTP_EMAIL = ""
SMTP_PASSWORD = ""
URL = "https://www.amazon.com/KD-Cricket-Supporter-Polyster-Material/dp/B07YNK3QG6/"
headers = {
        "User-Agent": "Defined",
        "Accept-Language": "en-US,en;q=0.5"
}


def scrape_price():
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    price = soup.find(name="span", class_="a-offscreen").getText()
    return float(price.replace("$", ""))


def send_email(price, receiver):
    message = f"Subject:New Low Price on Amazon!!\n\nLow price alert!Only ${price} to buy : \n{URL}"
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=SMTP_EMAIL, password=SMTP_PASSWORD)
        connection.sendmail(
                from_addr=SMTP_EMAIL, 
                to_addrs=receiver, 
                msg=message
                )

if __name__ == "__main__":
    receiver_email = ""
    price = scrape_price()
    # in this case if price less than 25 then send an email
    if price < 25:
        send_email(price, receiver_email)
    else:
        print("not today!")