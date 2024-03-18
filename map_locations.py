import pandas as pd
import folium


def plot_markers_from_csv(csv_file):
    df = pd.read_csv(csv_file)

    m = folium.Map(
        location=[df["Latitude"].iloc[0], df["Longitude"].iloc[0]], zoom_start=12
    )

    for index, row in df.iterrows():
        try:
            print(row["Latitude"], type(row["Latitude"]))
            # if row["Latitude"] == "nan" or row["Longitude"] == "nan":
            #     continue
            # Construct the popup content with Date, Time, Sponsor, Event, and Address
            popup_content = f"Date: {row['Date']}<br>"
            popup_content += f"Time: {row['Time']}<br>"
            popup_content += f"Sponsor: {row['Sponsor']}<br>"
            popup_content += f"Event: {row['Event & RSVP Link']}<br>"
            popup_content += f"Address: {row['Address']}"

            # Add marker to the map with popup content
            folium.Marker(
                location=[row["Latitude"], row["Longitude"]], popup=popup_content
            ).add_to(m)
        except ValueError:
            continue

    m.save("markers_map.html")


plot_markers_from_csv("lat_long_events.csv")
