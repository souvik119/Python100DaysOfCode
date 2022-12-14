import requests

#complete url is:
#https://opentdb.com/api.php?amount=10&type=boolean
#anything after ? is parameters

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]