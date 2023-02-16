# ===============================================
# ADD FUNCTION TO SEND EMAIL WHEN ISS IS OVERHEAD
# ===============================================

import requests
from datetime import datetime
from time import sleep

MY_LAT = 35.673909
MY_LONG = 139.667558

def iss_loc():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.strftime(datetime.now(), '%H')

while True:
    iss_latitude, iss_longitude = iss_loc()
    if iss_latitude > (MY_LAT - 5) and iss_latitude < (MY_LAT + 5) and iss_longitude > (MY_LONG -5) and iss_longitude < (MY_LONG + 5):
        if time_now > sunset and time_now < sunrise:
            # SEND AN EMAIL
            print("Look up! The ISS is flying above!")
            # print(f"My location: {MY_LAT}, {MY_LONG}")
            print(f"ISS location: {iss_latitude}, {iss_longitude}")
            False
    sleep(1)
