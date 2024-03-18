# Visualize Kubecon 2024 Parties

https://zwoefler.github.io/Visualize_Kubecon_Parties_2024/

Parties form: https://conferenceparties.com/kubeconeu24/

1. Get HTML table
2. Make csv out of it
3. Put on webpage
4. Make Map
5. show markers for each location
6. Make view per day
7. Click on marker revelas additional information


glhf


## How it works
SETUP DEV ENVIRONMENT:
1. Clone repo
2. Setup Python3 Virtual Env: `python3 -m venv Env`
3. Activate Virtual Env: `source Env/bin/activate`
4. Install requirements: `pip install -r requirements.txt`

GET DATA:
1. Run `python3 get_party_data.py`
2. This creates the `events.csv` which holds all events from the parties webpage
3. Run `python3 filter_event_data.py`
4. This filters empty rows in the `filtered_events.csv`
5. Run `python3 locate_locations.py`
6. Takes `filtered_events.csv` and returns the same csv with location data in `lat_long_events.csv`
7. Run `python3 map_locations.py`
8. THis creates the `event_locations_map.html` which can be included in the main webpage




## Lessons Learned
- GitHub Pages is easy to setup...: https://pages.github.com/#tutorial
- Have a stable internet connection... to receive the location data for addresses
- OpenStreetMap sucks ass... When you try to find "KaraFun Paris 3 Imp. Bonne Nouvelle" on `Nominatim` you won't find anything...
- Google API needs verification via VISA, that apparently doesn't work on the train

