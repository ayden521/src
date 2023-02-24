import mysql
import mysql.connector
db = mysql.connector.connect(
   user='root', password='password', host='localhost', database='mydb'
)

cur = db.cursor()
cur.execute("SELECT MAX(price) AS Max Price FROM activities;") 
max_result = cur.fetchall() 
#for i in max_result:
#    maximum = float(i[0])
#    print(maximum)

cur2 = db.cursor()
cur2.execute("SELECT AVG(price) AS Average Price FROM activities;")
ave_result = cur2.fetchall

cur3 = db.cursor()
cur3.execute("SELECT SUM(participants) as Total Participants FROM activities;" )
sum_result = cur3.fetchall

cur4 = db.cursor()
cur4.execute("SELECT type as Type from FROM activities;")
type_result = cur4.fetchall

# Close database connection
db.close()
