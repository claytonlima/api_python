import requests
from config.geocoding import GEOCODING_API_KEY

def get_origin_destiny_latitude_longitude(latitude, longitude):
    url = "https://api.opencagedata.com/geocode/v1/json?q=" + latitude + "+" + longitude + "&key=" + GEOCODING_API_KEY + "&language=pt&pretty=1"
    request_geo_data = requests.get(url).json()

    if request_geo_data['status']['code'] == 200:
        return request_geo_data['results'][0]['formatted']