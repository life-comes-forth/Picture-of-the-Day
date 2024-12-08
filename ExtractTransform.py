import requests
import Constants
from datetime import datetime

APIKey = Constants.key
URL = "https://api.nasa.gov/planetary/apod"
requestDate = datetime.today().strftime('%Y-%m-%d')

def fetch_apod(date):
    params = {"api_key": APIKey, "date": date}
    response = requests.get(URL, params = params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def transform_apod(data):
    #Formatting Date
    formatted_date = datetime.strptime(data["date"], "%Y-%m-%d").strftime("%d-%m-%Y")
    #Standardize filename
    filename = f"{formatted_date}_{data['title'].replace(' ', '_')}.jpg"
    return {"date": formatted_date, "title": data['title'] ,"filename": filename, "explanation": data["explanation"], "image_path": data["url"],}


