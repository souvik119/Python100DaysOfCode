import requests

SHEETY_ENDPT = "https://api.sheety.co/fa4f1e204344de78e87d85191574fdbc/flightDeals/prices"

class DataManager:
    
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for record in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": record["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPT}/{record['id']}", json=new_data)
            print(response.text)