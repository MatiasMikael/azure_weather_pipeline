import os
import subprocess
import logging

# Initialize logging
LOG_DIR = "5_logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    """Run the entire pipeline in the correct order."""
    try:
        # Step 1: Fetch weather data
        logging.info("Step 1: Fetching weather data...")
        print("Step 1: Fetching weather data...")
        subprocess.run(["python", "1_scripts/fetch_weather_data.py"], check=True)
        logging.info("Weather data fetched successfully.")
        print("Weather data fetched successfully.")

        # Step 2: Clean weather data
        logging.info("Step 2: Cleaning weather data...")
        print("Step 2: Cleaning weather data...")
        subprocess.run(["python", "1_scripts/clean_weather_data.py"], check=True)
        logging.info("Weather data cleaned successfully.")
        print("Weather data cleaned successfully.")

        # Step 3: Upload cleaned data to Azure Blob Storage
        logging.info("Step 3: Uploading cleaned data to Azure Blob Storage...")
        print("Step 3: Uploading cleaned data to Azure Blob Storage...")
        subprocess.run(["python", "1_scripts/upload_to_blob.py"], check=True)
        logging.info("Cleaned data uploaded successfully.")
        print("Cleaned data uploaded successfully.")

        # Step 4: Download data from Azure Blob Storage
        logging.info("Step 4: Downloading data from Azure Blob Storage...")
        print("Step 4: Downloading data from Azure Blob Storage...")
        subprocess.run(["python", "1_scripts/download_from_blob.py"], check=True)
        logging.info("Data downloaded successfully.")
        print("Data downloaded successfully.")

        # Step 5: Analyze weather data
        logging.info("Step 5: Analyzing weather data...")
        print("Step 5: Analyzing weather data...")
        subprocess.run(["python", "1_scripts/analyze_weather_data.py"], check=True)
        logging.info("Weather data analyzed successfully.")
        print("Weather data analyzed successfully.")

    except subprocess.CalledProcessError as e:
        logging.error(f"Error during pipeline execution: {e}")
        print(f"Error during pipeline execution: {e}")
        exit(1)

if __name__ == "__main__":
    run_pipeline()