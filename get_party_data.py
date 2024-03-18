from bs4 import BeautifulSoup
import requests
import csv

# Fetch the webpage
url = "https://conferenceparties.com/kubeconeu24/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table
table = soup.find('table')
print(table)



# Extract data and write to CSV
with open('events.csv', 'w', newline='') as csvfile:
    fieldnames = ['Date', 'Time', 'Sponsor', 'Event & RSVP Link', 'Location']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    current_date = ""
    for row in table.find_all('tr'):
        if row.find('h2'):  # Check for date row
            current_date = row.find('h2').text.strip()
        elif row.find_all('td', recursive=False) and len(row.find_all('td')) >= 4:  # Check for event row
            data = {}
            columns = row.find_all('td', recursive=False)
            data['Date'] = current_date
            data['Time'] = columns[0].text.strip()
            data['Sponsor'] = columns[1].text.strip()
            data['Event & RSVP Link'] = columns[2].text.strip()
            data['Location'] = columns[3].text.strip()
            writer.writerow(data)
