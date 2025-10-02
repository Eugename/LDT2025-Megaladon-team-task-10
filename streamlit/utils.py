import requests
import os
import locale
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

api_url = os.getenv("API_URL")


def get_entity(input):
    response = requests.post(
        f"{api_url}api/predict",
        json={"input": input},
        timeout=200
    )
    return response.json()
