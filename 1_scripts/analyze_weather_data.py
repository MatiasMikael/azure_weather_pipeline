import pandas as pd
import os
import logging

# Initialize logging
LOG_DIR = "5_logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "analyze_weather_data.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def analyze_weather_data(file_path, output_path):
    """Analyze weather data from a CSV file and save the results."""
    try:
        # Read the data
        df = pd.read_csv(file_path)

        # Extract information
        city = df["city"].iloc[0]
        temperature = df["temperature"].iloc[0]
        feels_like = df["feels_like"].iloc[0]
        humidity = df["humidity"].iloc[0]
        weather_description = df["description"].iloc[0]

        # Prepare analysis results
        results = [
            f"City: {city}",
            f"Temperature: {temperature:.2f}°C",  # Rounded to 2 decimals
            f"Feels like: {feels_like:.2f}°C",  # Rounded to 2 decimals
            f"Humidity: {humidity}%",
            f"Weather description: {weather_description}"
        ]
        if feels_like < temperature:
            results.append("The weather feels colder than the actual temperature.")
        else:
            results.append("The weather feels warmer or as warm as the actual temperature.")

        # Save results to a file
        os.makedirs("3_results", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as file:  # Ensuring special character support
            file.write("\n".join(results))
        logging.info(f"Analysis results saved to {output_path}")

        # Print results to console
        for line in results:
            print(line)

    except Exception as e:
        logging.error(f"Error analyzing data: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    input_path = os.path.join("2_data", "downloaded_cleaned_weather_data.csv")
    output_path = os.path.join("3_results", "weather_analysis.txt")
    analyze_weather_data(input_path, output_path)