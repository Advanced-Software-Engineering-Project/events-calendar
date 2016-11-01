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




class FacebookScraper:

    def get_groups(self):

        return

    def get_events(self, groups_file):
        start_date = datetime.datetime.now().strftime("%Y-%m-%d")
        events = []

        with open(filename) as data_file:
            pages_data = json.load(data_file)

            # For every Columbia Page:
            for i, page in enumerate(pages_data):
                pprint(page['node_id'])
                pprint(page['url'])

                url = 'https://graph.facebook.com/v2.8/'
                url = url + page['node_id']
                url = url + '/events?'
                url = url + 'since='
                url = url + start_date
                url = url + '&access_token=EAACEdEose0cBALFkO6rUmGl01Qt864YOXOWv67Lg2FgRQbsqeq8B3HnevZCFlTsW9jmuIX4nMedvZALi9DBLXj06O5K8b9AA3hazmm4UUAsXDcl5hZBEFHx6ZCiiEDFBi4peoF8Pxj7yyhPYqtmnv0x8m5JcGlBu7LfQtS6HywZDZD'
                url = url + '&debug=all&format=json&method=get&pretty=0&suppress_http_code=1'
                url = url + '&fields=name,place,start_time,description,cover,photos.limit(1),picture'

                response = requests.get(url, headers=headers)
                data = response.json()
                print(response.json())

                # Skipping some nodes that have urls instead of ids:
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
                    event['datetime'] = d['start_time']
                    if 'place' in d:
                        event['location'] = d['place']['name']
                    if 'cover' in d:
                        event['photo_url'] = d['cover']['source']

                    events.append(event)

                if i % 10 == 0:
                    print('\n\n\nFinished ' + str(i) + ' pages')
                    print('Events count: ' + str(len(events)) + '\n\n\n')

                    with open('events_data.json', 'w') as outfile:
                        json.dump(events, outfile)



if __name__ == "__main__":
    scraper = FacebookScraper()
    scraper.get_events('dummy')