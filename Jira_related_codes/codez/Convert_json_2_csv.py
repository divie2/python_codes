import json
import csv

# Read JSON data from file
with open('projects_last_6months.json', 'r') as json_file:
    data = json.load(json_file)

# Specify the CSV file path
csv_file_path = 'output1.csv'

# Write CSV data to file
with open(csv_file_path, 'w', newline='') as csv_file:
    # Extract all unique keys from the JSON data
    all_keys = set().union(*(d.keys() for d in data))

    # Create a CSV writer
    csv_writer = csv.writer(csv_file)

    # Write the header (field names)
    csv_writer.writerow(all_keys)

    # Write the data
    for row in data:
        # Create a list with values corresponding to the header
        csv_writer.writerow([row.get(key, "") for key in all_keys])

print(f'Conversion complete. CSV file saved at: {csv_file_path}')