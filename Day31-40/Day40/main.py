#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "SAN"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

#add user details
print("Welcome to Souvik's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
while True:
    email = input("What is your email?\n")
    confirm_email = input("Type your email again\n")
    if email == confirm_email:
        break
print("You are in the club!")
data_manager.add_new_user(first_name, last_name, email)


sheet_data = data_manager.get_destination_data()
user_data = data_manager.get_user_data()

# Check if IATA code field is empty, if it is, then get the value from FlightSearch class
if sheet_data[0]["iataCode"] == "":
    for record in sheet_data:
        record["iataCode"] = flight_search.get_destination_code(record["city"])
    
    #update iata code in the actual sheet
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for record in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        record["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is not None and flight.price < record["lowestPrice"]:
        notification_manager.send_sms(flight)
        notification_manager.notify_users(user_data, flight)