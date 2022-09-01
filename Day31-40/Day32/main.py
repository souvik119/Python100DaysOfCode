import smtplib
from sqlite3 import connect

my_email = ""
password = ""

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="", 
        msg="Subject:Hello\n\nThis is the body"
        )
