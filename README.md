# How these python files work.

activity_service.py gets the data from the API call and returns the activity from the API call

db_services.py inserts the data from the API call in activity_sercive.py into the DB. 
db_services.py pulls the data from the database that we later export into a csv file.

report_services.py writes the data pulled from db_services.py into a csv called data.csv
