# fetch data from api and inserts into db
from activity_service import get_activity_from_api
from db_service import insert_activity

activity = get_activity_from_api()
#print (activity)
insert_activity(activity)