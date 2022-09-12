import requests
import config

class DataManager:
    
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{config.SHEETY_BASE_URL}/prices")
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
            response = requests.put(url=f"{config.SHEETY_BASE_URL}/prices/{record['id']}", json=new_data)
            print(response.text)

    def get_user_data(self):
        response = requests.get(url=f"{config.SHEETY_BASE_URL}/users")
        data = response.json()
        self.destination_data = data["users"]
        return self.destination_data

    def add_new_user(self, first_name, last_name, email):
        new_user = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=f"{config.SHEETY_BASE_URL}/users", json=new_user)
        print(response.text)

