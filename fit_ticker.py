import os
import sys
import requests
import json

FIT_URL = r"https://fitathletic.com/wp-content/plugins/fit-occupancy/fit_occupancy_little-italy.json"

def main(argc,argv):
    response = requests.get(FIT_URL)
    availability = json.loads(response.content)
    available = int(availability.get('max')) - int(availability.get('current'))
    if availability.get('status') == 'open':
        print(f"Open - Availability: {available}")

if __name__ == "__main__":
    main(len(sys.argv),sys.argv)
