import requests
from datetime import datetime, timedelta

MY_LAT = 35.673909
MY_LON = 139.667558

def main():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LON,
        'formatted': 0
    }

    response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    day_length = data['results']['day_length']

    adjusted_sunrise = datetime.strptime((sunrise.split('T')[0] + " " + sunrise.split('T')[1].split('+')[0]), 
                                        '%Y-%m-%d %H:%M:%S') + timedelta(hours=9)
    adjusted_sunset = datetime.strptime((sunset.split('T')[0] + " " + sunset.split('T')[1].split('+')[0]), 
                                        '%Y-%m-%d %H:%M:%S') + timedelta(hours=9)

    now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    # print(type(now), type(adjusted_sunrise), sep=' ')

    print(f"Current time is: {now}")
    print(f"Sunrise is at: {adjusted_sunrise}")
    print(f"Sunset is at: {adjusted_sunset}")

if __name__ == "__main__":
    main()
