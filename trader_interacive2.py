import mysql
import mysql.connector
db = mysql.connector.connect(
   user='root', password='password', host='localhost', database='mydb'
)

cur = db.cursor()

cur.execute("SELECT MAX(price) AS Max Price FROM activities;")
  
result = cur.fetchall()
  
for i in result:
    maximum = float(i[0])
    print(maximum)

cur.execute("SELECT AVG(price) AS Average Price from activities;")
  
# Close database connection
db.close()
