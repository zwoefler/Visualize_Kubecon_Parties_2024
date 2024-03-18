import csv
import pandas as pd
from geopy.geocoders import Nominatim
import folium

# Load filtered events data
filtered_data = pd.read_csv('filtered_events.csv')
locations = filtered_data["Address"]

def locate_location(location):
    location_info = geolocator.geocode(location)
    if location_info:
        latitude = location_info.latitude
        longitude = location_info.longitude
        return latitude, longitude 

    return None, None

geolocator = Nominatim(user_agent="map_marker")
filtered_data["Latitude"], filtered_data["Longitude"] = zip(*filtered_data["Address"].apply(locate_location))
filtered_data.to_csv("lat_long_events.csv")

