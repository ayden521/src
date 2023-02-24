# pull data from the API call
import requests
import json
import mysql
api_resopnse = requests.get('http://www.boredapi.com/api/activity').text
response_info = json.loads(api_resopnse)
print (response_info)

# parse out the key pair values in the
# response_info json body so that we can later insert it into the db
for key in response_info:
    value = response_info[key]
    inserts = ("INSERT INTO activities ({}) VALUES '{}';".format(key, value))
    print (inserts)



# Serializing json
#json_object = json.dumps(response_info, indent=7)
#print (json_object)
 
# Writing to sample.json
#with open("sample.json", "w") as outfile:
#    outfile.write(json_object)

#TABLE_NAME = "activities"

#sqlstatement = ''
#with open ('sample.json','r') as f:
#    jsondata = json.loads(f.read())
#    print(jsondata)

#for json in json_object:
#    keylist = "("
#    valuelist = "("
#    firstPair = True
#    for key, value in json.items():
#        if not firstPair:
#            keylist += ", "
#            valuelist += ", "
#        firstPair = False
#        keylist += key
#        if type(value) in (str, unicode):
#            valuelist += "'" + value + "'"
#        else:
#            valuelist += str(value)
#    keylist += ")"
#    valuelist += ")"

#    sqlstatement += "INSERT INTO " + TABLE_NAME + " " + keylist + " VALUES " + valuelist + "\n"

#print(sqlstatement)
# now how to get these insert statemetns inserted into mysql
import mysql.connector

#establishing the connection (this is a fake connection)
connection = mysql.connector.connect(
   user='root', password='password', host='localhost', database='mydb'
)
#Creating a cursor object using the cursor() method
cursor = connection.cursor()

#Creating table as per requirement
sql ='''CREATE TABLE `activities` (
`activity` varchar(100) DEFAULT NULL,
`type` varchar(100) DEFAULT NULL,
`participants` INTEGER,
`price` INTEGER,
`link` varchar(100) DEFAULT NULL,
`key` varchar(100) DEFAULT NULL,
`accessibility` INTEGER,
`create_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);'''
cursor.execute(sql)
connection.commit()

# add the inserts from the API call
# I don't think I've done this right...
cursor.execute(inserts)
connection.commit()

#Closing the connection
connection.close()