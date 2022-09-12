import requests
from flight_data import FlightData
import config

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        """Returns IATA code for destination city"""
        search_headers = {
            "apikey": config.TEQUILA_API_KEY
        }
        search_params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{config.TEQUILA_BASE_URL}/locations/query", params=search_params, headers=search_headers)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    
    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        search_headers = {
            "apikey": config.TEQUILA_API_KEY
        }
        search_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{config.TEQUILA_BASE_URL}/v2/search",
            headers=search_headers,
            params=search_params,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

