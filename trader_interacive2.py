import csv
import mysql
import mysql.connector
db = mysql.connector.connect(
   user='root', password='password', host='localhost', database='mydb'
)

cur = db.cursor()
sql = "SELCT type, MAX(price), AVG(price), SUM(participants) FROM activities GROUP BY type;"
cur.execute(sql) 
results = cur.fetchall() 

# Close database connection
db.close()

# Create the csv file
with open('data.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Add the header/column names
    header = ['Type', 'Max Price', 'Average Price', 'Total Participants']
    writer.writerow(header)
    # Iterate over `results`  and  write to the csv file
    for row in results:
        writer.writerow(row)
