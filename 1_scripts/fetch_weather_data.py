import requests
import pandas as pd
import os
import logging
from dotenv import load_dotenv

# Initialize logging
LOG_DIR = "5_logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "fetch_weather_data.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# API Configuration
API_KEY = "c71c9d963510d86ba41d8e907a393042"
API_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    """Fetch weather data for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        logging.info(f"Weather data fetched successfully for city: {city}")
        return response.json()
    else:
        logging.error(f"API error: {response.status_code} for city: {city}")
        raise Exception(f"API error: {response.status_code}")

def save_weather_data_to_csv(data, file_path):
    """Save weather data to a CSV file."""
    df = pd.DataFrame([data])
    df.to_csv(file_path, index=False)
    logging.info(f"Weather data saved to {file_path}")

if __name__ == "__main__":
    city = "Helsinki"
    file_path = os.path.join("2_data", "weather_data.csv")
    
    try:
        logging.info(f"Fetching weather data for city: {city}")
        weather_data = fetch_weather_data(city)
        save_weather_data_to_csv(weather_data, file_path)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"Error: {e}")