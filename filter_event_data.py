import csv

# Read the CSV file
with open('events.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    events_data = list(reader)


header = events_data[0]
# Filter out lines with specific entries or empty last 4 elements
filtered_data = [row for row in events_data if row[-4:] != ['Time', 'Sponsor', 'Event & RSVP Link', 'Location'] and row[-4:] != ['', '', '', '']]
filtered_data.insert(0, header)

# Write the filtered data back to the CSV file
with open('filtered_events.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(filtered_data)

