import requests
# from twilio.rest import Client
# import os

MY_LAT = 35.673909
MY_LON = 139.667558

api_key = "f15eea05633933b7617987c2baf79540"
endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'appid': api_key,
    # 'exclude': 'current,minutely,daily'
}

response = requests.get(url=endpoint, params=parameters)
response.raise_for_status()
print(response)

data = response.json()

print(data)