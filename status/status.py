import requests
import json
from datetime import datetime

def get_status():
    print("Get EVE Status")
    baseUrl = 'https://esi.evetech.net/latest/status/'
    server='tranquility'
    response = requests.get(baseUrl + '?datasource=' + server)
    data = response.json()
    print(data)

    # Parse date and time
    now = datetime.utcnow().strftime('%Y-%m-%d %H%M')
    data['extract_time'] = now

    filename = 'output\{}.json'.format(server)
    print(filename)
    with open(filename, 'a') as file:
        json.dump(data, file)


if __name__ == '__main__':
    get_status()

