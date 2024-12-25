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
    filename=os.path.join(LOG_DIR, "upload_to_blob.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def upload_to_blob(file_path, blob_name):
    """Upload file to Azure Blob Storage."""
    try:
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
            logging.info(f"{blob_name} uploaded to Azure Blob Storage.")
            print(f"{blob_name} uploaded successfully.")
    except Exception as e:
        logging.error(f"Error uploading file to Azure Blob Storage: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = os.path.join("2_data", "cleaned_weather_data.csv")
    blob_name = "cleaned_weather_data.csv"
    upload_to_blob(file_path, blob_name)