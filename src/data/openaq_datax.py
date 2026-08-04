# ===== IMPORTS =====
import os

from dotenv import load_dotenv
from openaq import OpenAQ
from datetime import date

# ===== CONSTANTS =====
ENV_PATH = ".env"
load_dotenv(dotenv_path = ENV_PATH)

api_key = os.getenv("openaq_apikey")

# ===== MAIN =====
def main():
    client = OpenAQ(api_key = api_key)

    # Single location with location id
    location = client.locations.get(2178) 
    print("===== SINGLE LOCATION =====")
    print(location.results[0].name)
    
    # get lists of location
    locations = client.locations.list(
        parameters_id=2,
        coordinates=(15.81207, 102.02316),
        radius=1000,
        limit=1000
    )

    locations_id = locations.results[0].id
    print("\n===== LOCATIONS ID =====")
    print(locations_id)
    
    # Get PM2.5-sensor 
    sensors = client.locations.sensors(locations_id)
    pm25_sensors_id = 0

    for sensor in sensors.results:
        if "pm25" in sensor.name:
            pm25_sensors_id = sensor.id
            break
    
    print("\n===== SENSORS =====")
    print(sensors)
    
    # get measurement
    response = client.measurements.list(pm25_sensors_id,
                                    data="days",
                                    date_from=date(2025, 1, 1),
                                    date_to=date(2025, 12, 31)
                                    )

    measurements = response.results
    
    print("\n===== MEASUREMENTS =====")
    print(measurements)

    client.close()


# ===== SYSTEM CALLING =====
if __name__ == "__main__":
    main()
else:
    print(f"Importing {__name__}...")