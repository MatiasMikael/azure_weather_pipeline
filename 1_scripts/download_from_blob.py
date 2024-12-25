import os
import logging
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "weather-data"

# Initialize logging
LOG_DIR = "5_logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "download_from_blob.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def download_from_blob(blob_name, download_path):
    """Download a file from Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

        with open(download_path, "wb") as file:
            file.write(blob_client.download_blob().readall())
            logging.info(f"{blob_name} downloaded from Azure Blob Storage to {download_path}.")
            print(f"{blob_name} downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading file from Azure Blob Storage: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    blob_name = "cleaned_weather_data.csv"
    download_path = os.path.join("2_data", "downloaded_cleaned_weather_data.csv")
    download_from_blob(blob_name, download_path)