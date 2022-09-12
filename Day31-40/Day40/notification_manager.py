from twilio.rest import Client
import config
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(config.TWILIO_SID, config.TWILIO_AUTH_TOKEN)

    def send_sms(self, flight):
        body_text = f"""Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}.\n
        https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"""
        message = self.client.messages.create(
            body=body_text,
            from_=config.TWILIO_VIRTUAL_NUMBER,
            to=config.TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def notify_users(self, users, flight):
        for user in users:
            receiver = user["email"]
            message=f"Subject:New Low Price Flight!\n\nLow price alert!Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            self.send_email(receiver, message)

    def send_email(self, receiver, message):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=config.SMTP_EMAIL, password=config.SMTP_PASSWORD)
            connection.sendmail(
                from_addr=config.SMTP_EMAIL, 
                to_addrs=receiver, 
                msg=message
                )
