import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('_data/events.csv', delimiter=";")

# Export the DataFrame to an HTML table
html_table = df.to_html(index=False)

# Write the HTML table to a file
with open('events_table.html', 'w') as file:
    file.write(html_table)
