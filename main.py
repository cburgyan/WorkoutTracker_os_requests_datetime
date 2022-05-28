import os
import requests
import datetime


"""This program takes in a natural language phrase about exercise (eg "ran for 2 hours") from the console,
then gets an exercise classification (eg "running"), calories burned, and duration (eg "120 minutes") back
from nutritionix.com, then sends this info to sheety.co which in turn adds the information into a google
docs spreadsheet (looks like excel).
"""

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")
NUTRITIONIX_ENDPOINT = os.environ.get("NUTRITIONIX_ENDPOINT"
                                      "")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_KEY = os.environ.get("SHEETY_KEY")
SHEETY_ID = ""
EXERCISE_EXTENSION = "natural/exercise"

GENDER = "male"
WEIGHT_KG = os.environ.get("WEIGHT_KG")
HEIGHT_CM = os.environ.get("HEIGHT_CM")
AGE = os.environ.get("AGE")

nutri_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
    #"x-remote-user-id": 0
}

sheety_headers = {
    "Authorization": SHEETY_KEY
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
        nutri_response = requests.post(url=f"{NUTRITIONIX_ENDPOINT}/{EXERCISE_EXTENSION}",
                                       json=nutri_params,
                                       headers=nutri_headers).json()
        print(nutri_response)
        exercise = nutri_response["exercises"][0]["name"]
        print(exercise)
        duration = nutri_response["exercises"][0]["duration_min"]
        print(duration)
        calories = nutri_response["exercises"][0]["nf_calories"]
        print(calories)
        today = datetime.datetime.now()
        date = today.strftime("%d/%m/%Y")
        print(date)
        time = today.strftime("%H:%M:%S")
        print(time)

        sheety_params = {
            "workout": {
                "exercise": exercise,
                "duration": duration,
                "calories": calories,
                "time": time,
                "date": date
            }
        }

        sheety_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=sheety_params)
        print(sheety_response.text)
