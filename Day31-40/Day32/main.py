# import smtplib

# my_email = ""
# password = ""

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="", 
#         msg="Subject:Hello\n\nThis is the body"
#         )



##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""


def today_month_day():
    """Returns today's month and day"""
    now = dt.datetime.now()
    return now.month, now.day


def check_spreadsheet(today_month, today_date):
    """Returns the name and email if month and day matches any records in csv"""
    df = pandas.read_csv("birthdays.csv")
    for index, row in df.iterrows():
        if today_month == row["month"] and today_date == row["day"]:
            send_email(row["name"], row["email"])

def send_email(name, email):
    """Sends email based on supplied name and email"""
    letter_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_num}.txt", mode="r") as data_file:
        data = data_file.read()
        data = data.replace("[NAME]", name)
    
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=email, 
            msg=f"Subject:Happy Birthday\n\n{data}"
            )

def main():
    today_month, today_date = today_month_day()
    check_spreadsheet(today_month, today_date)

main()