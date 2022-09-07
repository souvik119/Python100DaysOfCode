import requests
from twilio.rest import Client
import os

API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = 51.507351
MY_LONG = -0.127758
ACCOUNT_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
    .create(
         body="Carry umbrella",
         from_="+17173668974",
         to="+16194306455"
     )
    print(message.status)