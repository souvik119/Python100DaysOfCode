import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""

GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = 162.56
AGE = 30

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_TEXT = input("Tell me which exercises you did: ")
SHEET_ENDPOINT = "https://api.sheety.co/fa4f1e204344de78e87d85191574fdbc/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": EXERCISE_TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=exercise_parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": ""
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_params, headers=bearer_headers)
    print(sheet_response.text)