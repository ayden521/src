# How these python files work.

activity_service.py gets the data from the API call and returns the activity from the API call

db_services.py inserts the data from the API call in activity_sercive.py into the DB. 
db_services.py pulls the data from the database that we later export into a csv file.

report_services.py writes the data pulled from db_services.py into a csv called data.csv

report_acticity.py calls the function get_activity_summary from db_service.py and passes that info into the function write_activities_to_file from report_service.py.

fetch_activity.py calls the function get_activity_from_api from activity_service.py and passed that info into the function insert_activity from db_service.py

# setting up cronjob
crontab -e
* * * * * /usr/bin/python3 /Users/ayden/my_code_projects/trader_interactive/fetch_activity.py 
* * * * * /usr/bin/python3 /Users/ayden/my_code_projects/trader_interactive/report_activity.py 


