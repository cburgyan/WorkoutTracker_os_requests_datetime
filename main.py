import os
import requests


APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
NUTRITIONIX_END_POINT = "https://trackapi.nutritionix.com/v2"
EXERCISE_EXTENSION = "natural/exercise"

GENDER = "male"
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    #"x-remote-user-id": 0
}

user_response = ""
while user_response != "exit":
    user_response = input("Tell me which exercises you did: ")
    if user_response != "exit":
        nutri_params = {
            "query": user_response,
            "gender": GENDER,
            "weight_kg": WEIGHT_KG,
            "height_cm": HEIGHT_CM,
            "age": AGE
        }
        nutri_response = requests.post(url=f"{NUTRITIONIX_END_POINT}/{EXERCISE_EXTENSION}",
                                       json=nutri_params,
                                       headers=nutri_headers)
        print(nutri_response.text)
