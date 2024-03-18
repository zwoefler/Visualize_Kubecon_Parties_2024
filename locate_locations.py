import csv
import pandas as pd
from geopy.geocoders import Nominatim
import folium

# Load filtered events data
filtered_data = pd.read_csv('filtered_events.csv')
locations = filtered_data["Address"]

# Initialize geocoder
geolocator = Nominatim(user_agent="map_marker")

mymap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

for location in locations:
    location_info = geolocator.geocode(location)
    if location_info:
        lat = location_info.latitude
        lon = location_info.longitude
        folium.Marker([lat, lon], popup=location).add_to(mymap)


mymap.save('event_locations_map.html')
