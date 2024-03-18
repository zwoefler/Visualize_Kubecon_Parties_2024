import pandas as pd
import folium

def plot_markers_from_csv(csv_file):
    df = pd.read_csv(csv_file)

    m = folium.Map(location=[df['Latitude'].iloc[0], df['Longitude'].iloc[0]], zoom_start=12)

    for index, row in df.iterrows():
        if row["Latitude"] or row["Longitude"] == :wq

        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Address']).add_to(m)

    m.save('markers_map.html')

plot_markers_from_csv('lat_long_events.csv')
