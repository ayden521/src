import requests
import json

def get_activity_from_api():
    api_response = requests.get('http://www.boredapi.com/api/activity').text
    activity = json.loads(api_response)
    return activity






