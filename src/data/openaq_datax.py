# ===== IMPORTS =====
import os

from dotenv import load_dotenv
from openaq import OpenAQ

# ===== CONSTANTS =====
ENV_PATH = ".env"
load_dotenv(dotenv_path = ENV_PATH)

api_key = os.getenv("openaq_apikey")

# ===== MAIN =====
def main():
    client = OpenAQ(api_key = api_key)

    location = client.locations.get(2178)

    client.close()

    print(location.results[0].name)

# ===== SYSTEM CALLING =====
if __name__ == "__main__":
    main()
else:
    print(f"Importing {__name__}...")