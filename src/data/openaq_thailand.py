# ===== IMPORTS =====
import os

import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
from openaq import OpenAQ
from typing import List, Tuple

# ===== CONSTANTS =====
ENV_PATH = ".env"
load_dotenv(dotenv_path = ENV_PATH)

api_key = os.getenv("openaq_apikey")

# ===== FUNCTIONS =====
def get_coord(location_list: List) -> Tuple[List, List]:
    """Get the latitude and longitude of each location in the given location_list.

    Args:
        location_list (List): a list containing locations.

    Returns:
        Tuple[List, List]: latitude and longitude of each location.
    """
    lat: List = []
    long: List = []
    
    for location in location_list:
        coord = location.coordinates
        lat.append(coord.latitude)
        long.append(coord.longitude)

    return lat, long

# ===== MAIN =====
def main():
    with OpenAQ(api_key = api_key) as client:
    
        # get lists of location in Thailand
        locations = client.locations.list(
            iso = "TH"
        )
        
        country_name = locations.results[0].country.name
        print(f"Country Name: {country_name}.")
        print(f"Total number of locations in {country_name}: {len(locations.results)}.")
        
        lat, long = get_coord(locations.results)
        
        for iter in range(3):
            print()
            location = locations.results[iter]
            print(f"# {location.name}'s (Location ID = {location.id}) available sensors:")
            for sensor in location.sensors:
                print(f"(Sensor id = {sensor.id}, {sensor.name}, {sensor.parameter.id}, {sensor.parameter.name}, {sensor.parameter.units}, {sensor.parameter.display_name})")
        
        # A sensor from Phahol Yothin Rd., Khet Chatuchak
        SENSOR_ID = 92 # No latest information. Maybe it's out of service?
        sensor_info = client.sensors.get(SENSOR_ID).results[0]
        
        print(f"\nThe sensor with ID {sensor_info.id} measures {sensor_info.parameter.display_name} in units {sensor_info.parameter.units}.")
        print("The statistical summary is as follows:")
        print(sensor_info.summary)
        

# ===== SYSTEM CALLING =====
if __name__ == "__main__":
    main()
else:
    print(f"Importing {__name__}...")