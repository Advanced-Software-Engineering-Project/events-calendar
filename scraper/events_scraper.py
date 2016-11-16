import datetime
import requests

import json
import os
from pprint import pprint


headers = {
    'origin': 'https://developers.facebook.com',
    'dnt': '1',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'accept-language': 'en-US,en;q=0.8,fr;q=0.6',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'referer': 'https://developers.facebook.com/',
    'authority': 'graph.facebook.com',
}

fileDir = os.path.dirname(os.path.realpath('__file__'))
pages_file = os.path.join(fileDir, 'scraper/data/pages_data.json')

# Grab API key
key_response = requests.get('https://graph.facebook.com/oauth/access_token?type=client_cred&client_id=355046878181225&client_secret=c6f4a196e8184f469515fdad16ff486d', headers=headers)
key  = key_response.text.split('=')[1]


def get_events():
    start_date = datetime.datetime.now().strftime("%Y-%m-%d")
    events = []

    with open(pages_file) as data_file:
        pages_data = json.load(data_file)

        # For every Columbia Page:
        for i, page in enumerate(pages_data):
            pprint(page['group_name'])

            url = 'https://graph.facebook.com/v2.8/'
            url = url + str(page['group_id'])
            url = url + '/events?'
            url = url + 'since='
            url = url + start_date
            url = url + '&access_token=' + 'EAAFC6csNd2kBAA38gHLzPeR4rNpMYgKaecy9KejLFWTOsx1RznYgHSBlvJBbslS5XTcdVFHPpOmMFuJuoDLjEfAYZCIIxKQ13T2ZCWrVa03KdgGyITlHTUQPYgWfZBFUln0ZBaTwpbqrQ0YgZBOJC'
            url = url + '&debug=all&format=json&method=get&pretty=0&suppress_http_code=1'
            url = url + '&fields=name,place,start_time,description,cover,photos.limit(1),picture'

            response_data = requests.get(url, headers=headers).json()
            print(response_data)

            if 'error' in response_data:
                continue

            # Add all that Page's events:
            for d in response_data['data']:
                event = {
                    'id': d['id'],
                    'title': d['name'],
                    'datetime': d['start_time'],
                    'group_id': page['group_id'],
                    'group': page['group_name'],
                    'group_url': page['group_url'],
                }

                if 'description' in d:
                    event['description'] = d['description']
                if 'place' in d:
                    event['location'] = d['place']['name']
                if 'cover' in d:
                    event['photo_url'] = d['cover']['source']

                events.append(event)

            if i % 10 == 0:
                print('\n\n\nFinished ' + str(i) + ' pages')
                print('Events count: ' + str(len(events)) + '\n\n\n')

                with open('scraper/data/events_data.json', 'w') as outfile:
                    json.dump(events, outfile)


if __name__ == "__main__":
    get_events()