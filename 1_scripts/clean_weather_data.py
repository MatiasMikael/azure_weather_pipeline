import pandas as pd
import os
import logging

# Initialize logging
LOG_DIR = "5_logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "clean_weather_data.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def clean_weather_data(input_path, output_path):
    """Clean and transform weather data."""
    try:
        raw_data = pd.read_csv(input_path)
        flat_data = {
            "city": raw_data["name"].iloc[0],
            "latitude": eval(raw_data["coord"].iloc[0])["lat"],
            "longitude": eval(raw_data["coord"].iloc[0])["lon"],
            "temperature": eval(raw_data["main"].iloc[0])["temp"],
            "feels_like": eval(raw_data["main"].iloc[0])["feels_like"],
            "pressure": eval(raw_data["main"].iloc[0])["pressure"],
            "humidity": eval(raw_data["main"].iloc[0])["humidity"],
            "weather": eval(raw_data["weather"].iloc[0])[0]["main"],
            "description": eval(raw_data["weather"].iloc[0])[0]["description"],
            "wind_speed": eval(raw_data["wind"].iloc[0])["speed"],
            "country": eval(raw_data["sys"].iloc[0])["country"]
        }
        df = pd.DataFrame([flat_data])
        df.to_csv(output_path, index=False)
        logging.info(f"Cleaned weather data saved to {output_path}")
    except Exception as e:
        logging.error(f"Error cleaning weather data: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    input_path = os.path.join("2_data", "weather_data.csv")
    output_path = os.path.join("2_data", "cleaned_weather_data.csv")
    clean_weather_data(input_path, output_path)