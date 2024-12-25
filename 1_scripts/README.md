1. **fetch_weather_data.py**
Fetches weather data from the OpenWeather API and saves it as raw data in CSV format in the folder 2_data.

2. **clean_weather_data.py**
Cleans the raw data and saves it as a refined CSV file in the folder 2_data with the name cleaned_weather_data.csv.

3. **upload_to_blob.py**
Uploads the cleaned data to Azure Blob Storage in the container named weather-data.

4. **download_from_blob.py**
Downloads the file from Azure Blob Storage and saves it locally in the folder 2_data with the name downloaded_cleaned_weather_data.csv.

5. **analyze_weather_data.py**
Analyzes the downloaded cleaned data and saves the results in the folder 3_results with the name weather_analysis.txt. Also creates a log file.

6. **run_pipeline.py**
Executes all the above scripts in the correct order and saves a log file named pipeline.log in the folder 5_logs.