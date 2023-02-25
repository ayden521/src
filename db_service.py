import mysql
import mysql.connector

def insert_activity(activity):
    activity_name = activity["activity"]
    type = activity["type"]
    participants = activity["participants"]
    price = activity["price"]
    link = activity["link"]
    key = activity["key"]
    accessibility = activity["accessibility"]

    insert = f"""INSERT INTO `activities`.`activities`
    (`activity`,
    `type`,
    `participants`,
    `price`,
    `link`,
    `key`,
    `accessibility`)
    VALUES
    ('{activity_name}',
    '{type}',
    {participants},
    {price},
    '{link}',
    {key},
    {accessibility}
    );"""

    # establishing the connection 
    connection = mysql.connector.connect(
    user='activity_app', password='Activity21', host='db4free.net', database='activities'
    )
        
    #Creating a cursor object using the cursor() method
    cursor = connection.cursor()
    # add the inserts from the API call
    cursor.execute(insert)
    connection.commit()

    #Closing the connection
    connection.close()


def get_activity_summary():
    connection = mysql.connector.connect(
    user='activity_app', password='Activity21', host='db4free.net', database='activities'
    )

    cur = connection.cursor()
    sql = "Select type, MAX(price), AVG(price), SUM(participants) FROM activities GROUP BY type;"
    cur.execute(sql) 
    results = cur.fetchall() 

    # Close database connection
    connection.close()
    return results
