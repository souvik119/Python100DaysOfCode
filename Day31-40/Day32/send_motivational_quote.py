import datetime as dt
import smtplib
import random


MY_EMAIL = ""
MY_PASSWORD = ""
SEND_TO = ""

def get_day_of_week():
    """Returns day of the week as integer, week starts from 0 (Monday)"""
    now = dt.datetime.now()
    return now.weekday()

def quote_list():
    """Returns a list of quotes from quotes.txt"""
    with open("quotes.txt", mode="r") as data_file:
        quotes = data_file.readlines()

    return quotes

def send_email(email_message):
    """Sends email to sender based on message and other sender details provided"""
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=SEND_TO, 
            msg=f"Subject:Monday Motivation\n\n{email_message}"
            )


def main():
    weekday = get_day_of_week()
    quotes = quote_list()
    quote_choice = random.choice(quotes)
    if weekday == 3:
        send_email(quote_choice)

main()