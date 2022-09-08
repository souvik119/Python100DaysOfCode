import requests
from datetime import datetime
import random

USERNAME = "souvikg"
TOKEN = "cwryrwi27r38745hasdhfd43"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

#create a user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# since user already created cannot run this line again and again
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)


# Create a new graph on pixela
graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}
#request header is used for authentication
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

# Fill a pixel in the graph
day = 1
month = 9
year = 2022
quantity = ["45", "30", "15", "0", "60"]

for _ in range(1, 8):
    today = datetime(year=year, month=month, day=day)
    pixel_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": random.choice(quantity)
    }
    response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
    print(response.text)
