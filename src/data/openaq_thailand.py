# ===== IMPORTS =====
import os

import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
from openaq import OpenAQ

# ===== CONSTANTS =====
ENV_PATH = ".env"
load_dotenv(dotenv_path = ENV_PATH)

api_key = os.getenv("openaq_apikey")

# ===== MAIN =====
def main():
    client = OpenAQ(api_key = api_key)
    
    # get lists of location in Thailand
    locations = client.locations.list(
        iso = "TH"
    )
    
    country_name = locations.results[0].country.name
    print(f"Country Name: {country_name}.")
    print(f"Total number of locations in {country_name}: {len(locations.results)}.")
    
    lat = []
    long = []

    for location in locations.results:
        coord = location.coordinates
        lat.append(coord.latitude)
        long.append(coord.longitude)
    
    client.close()

# ===== SYSTEM CALLING =====
if __name__ == "__main__":
    main()
else:
    print(f"Importing {__name__}...")