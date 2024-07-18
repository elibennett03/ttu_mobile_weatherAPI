import requests
import json
from datetime import datetime, timedelta, timezone

api_key = "grnvOEg0pA3JJ7QXED2CwyY8vb4wLr2i"
lat = 36.174809
lon = -85.505710

def fetch_weather(api_key, lat, lon):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={lat},{lon}&timesteps=1h&apikey={api_key}"
    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        response.raise_for_status()

def filter_next_24_hours(data):
    current_time = datetime.now(timezone.utc)
    next_24_hours = current_time + timedelta(hours=24)

    filtered_data = [
        item for item in data['timelines']['hourly']
        if current_time <= datetime.fromisoformat(item['time']).replace(tzinfo=timezone.utc) <= next_24_hours
    ]

    return filtered_data

def main(api_key, lat, lon):
    weather_data = fetch_weather(api_key, lat, lon)

    # Print the entire response to understand its structure
    print(json.dumps(weather_data, indent=4))

    filtered_data = filter_next_24_hours(weather_data)

    with open('weather_data.json', 'w') as data_file:
        json.dump(filtered_data, data_file, indent=4)

    print(json.dumps(filtered_data, indent=4))

# Run the script with the variables set above
main(api_key, lat, lon)
