import requests as req 
import json
import time

api_url = "https://api.open-meteo.com/v1/forecast"

session = req.Session()
session.headers.update({"User-Agent": "WeatherClient/1.0"})
params = {
    "latitude": 51.5072,
    "longitude": -0.1276,
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "auto",
}
try:
    response = session.get(api_url, params=params,timeout=50)
    response.raise_for_status()
    print("Loaded successfully....")
    time.sleep(2)
    data = response.json()
    daily_data = data["daily"]

    dates = daily_data["time"]
    max_temps = daily_data["temperature_2m_max"]
    min_temps = daily_data["temperature_2m_min"]

    simplified = []

    for i in range(len(dates)):
        simplified.append({
            "date": dates[i],
            "temp_max": max_temps[i],
            "temp_min": min_temps[i]
        })
    with open("data.json", 'w') as d:
        json.dump(simplified, d,indent=4)
        time.sleep(2)
        print("Data has been saved successfully")
except req.exceptions.Timeout:
    print("Request timed out")

except req.exceptions.HTTPError as e:
    print("HTTP error:", e)
except Exception as e:
    print("You encountered an error", e)


