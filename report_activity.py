# gets info from db and writes to the csv
from report_service import write_activities_to_file
from db_service import get_activity_summary

summary = get_activity_summary()
write_activities_to_file(summary)
