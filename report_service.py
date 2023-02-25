import csv

def write_activities_to_file(activity_summary):

    # Create the csv file
    with open('data.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        # Add the header/column names
        header = ['Type', 'Max Price', 'Average Price', 'Total Participants']
        writer.writerow(header)
        # Iterate over `results`  and  write to the csv file
        for row in activity_summary:
            writer.writerow(row)
