import csv
import itertools
import time

# Script builds a list of tuples to export to 'cleaned_trips_gdrive.csv'
all_trips = []

# Import delivery_geography.CSV and setup output file
with open('trips_gdrive.csv', 'rt') as input_file, open('cleaned_trips_gdrive.csv', 'wt', newline='') as output_file:

    data_reader = csv.reader(input_file, delimiter=',')
    data_writer = csv.writer(output_file)
    data_writer.writerow(["trip_id", 
                            "date", 
                            "retailer", 
                            "brand", 
                            "user_id", 
                            "item_spend", 
                            "item_units"])

    # Skip the header row of the input file
    next(data_reader, None)

    for row in data_reader:

        if "$" in row[5]:
            row[5] = int(row[5][1:])

        row[6] = int(row[6])
        all_trips.append(row)

    data_writer.writerows(all_trips)