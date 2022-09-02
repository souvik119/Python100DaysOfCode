import requests
import datetime as dt

MY_LAT = 32.715736
MY_LONG = -117.161087

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data["results"]["sunrise"])

time_now = dt.datetime.now()
