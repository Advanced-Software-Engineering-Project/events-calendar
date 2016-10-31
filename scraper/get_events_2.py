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
filename = os.path.join(fileDir, 'data/pages_with_ids.json')

start_date = datetime.datetime.now().strftime("%Y-%m-%d")
print(start_date)
events = []
i = 0
with open(filename) as data_file:
    pages_data = json.load(data_file)

    # For every Columbia Page:
    for page in pages_data:
        pprint(page['node_id'])
        pprint(page['url'])

        response = requests.get('https://graph.facebook.com/v2.8/' + page['node_id'] + '/events?' + 'since=' + start_date + '&access_token=EAACEdEose0cBALFkO6rUmGl01Qt864YOXOWv67Lg2FgRQbsqeq8B3HnevZCFlTsW9jmuIX4nMedvZALi9DBLXj06O5K8b9AA3hazmm4UUAsXDcl5hZBEFHx6ZCiiEDFBi4peoF8Pxj7yyhPYqtmnv0x8m5JcGlBu7LfQtS6HywZDZD&debug=all&format=json&method=get&pretty=0&suppress_http_code=1&fields=name,place,start_time,description,cover,photos.limit(1),picture', headers=headers)
        data = response.json()
        print(response.json())

        # Hack for skipping some nodes that have urls as ids:
        if 'http' in page['node_id']:
            continue

        # Add all that Page's events:
        for d in response.json()['data']:
            event = {}
            event['id'] = d['id']
            event['title'] = d['name']
            event['page_id'] = page['node_id']
            event['group_url'] = page['url']
            if 'description' in d:
                event['description'] = d['description']
            event['start_time'] = d['start_time']
            if 'place' in d:
                event['location'] = d['place']['name']
            if 'cover' in d:
                event['photo_url'] = d['cover']['source']

            events.append(event)

        i = i + 1
        if i % 10 == 0:
            print('\n\n\ndone with ' + str(i) + ' pages')
            print('events count: ' + str(len(events)) + '\n\n\n')

            with open('events_data.json', 'w') as outfile:
                json.dump(events, outfile)

