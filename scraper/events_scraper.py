#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for fetching new Columbia Events from Facebook
"""
# pylint: disable=E1101, E1120

import datetime
import json
import os

from pprint import pprint
import requests


HEADERS = {
    'origin': 'https://developers.facebook.com',
    'dnt': '1',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'accept-language': 'en-US,en;q=0.8,fr;q=0.6',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '53.0.2785.143 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'referer': 'https://developers.facebook.com/',
    'authority': 'graph.facebook.com',
}

FILE_DIR = os.path.dirname(os.path.realpath('__file__'))
PAGES_FILE = os.path.join(FILE_DIR, 'scraper/data/pages_data_3.json')

# Grab API key
KEY_RESPONSE = requests.get('https://graph.facebook.com/oauth/access_'
                            'token?type=client_cred&client_id=355046878'
                            '181225&client_secret=c6f4a196e8184f469515fd'
                            'ad16ff486d', headers=HEADERS)

json_resp = json.loads(KEY_RESPONSE.text)
KEY = json_resp['access_token']

class EventsScraper:

    def __init__(self, test_pages_file):
        """
        Initialize the EventsScraper
        :param test_pages_file: optional test data file with pages data for testing purposes
        :return:
        """
        self.pages_file = PAGES_FILE
        if test_pages_file:
            self.pages_file = test_pages_file

    def get_events(self):
        """
        Starts the scrape process from the FB api
        :return:
        """
        start_date = datetime.datetime.now().strftime("%Y-%m-%d")
        events = []

        with open(self.pages_file) as data_file:
            pages_data = json.load(data_file)

            # For every Columbia Page:
            for i, page in enumerate(pages_data):
                pprint(page['group_name'])

                url = 'https://graph.facebook.com/v2.8/'
                url += str(page['group_id'])
                url += '/events?'
                url += 'since='
                url += start_date
                url += '&access_token=' + '355046878181225|hoplLUPRx-cCdXfqDOByCujc4-w'
                url += '&debug=all&format=json&method=get&pretty=0&suppress_http_code=1'
                url += '&fields=name,place,start_time,description,cover,photos.limit(1),picture'

                response_data = requests.get(url, headers=HEADERS).json()
                print response_data

                if 'error' in response_data:
                    continue

                # Add all that Page's events:
                for dat in response_data['data']:
                    event = {
                        'id': dat['id'],
                        'title': dat['name'],
                        'datetime': dat['start_time'],
                        'group_id': page['group_id'],
                        'url': 'https://www.facebook.com/events/' + dat['id'],
                    }

                    if 'description' in dat:
                        event['description'] = dat['description']
                    if 'place' in dat:
                        event['location'] = dat['place']['name']
                    if 'cover' in dat:
                        event['photo_url'] = dat['cover']['source']

                    events.append(event)

                if i % 10 == 0:
                    print '\n\n\nFinished ' + str(i) + ' pages'
                    print 'Events count: ' + str(len(events)) + '\n\n\n'

                    with open('scraper/data/events_data.json', 'w') as outfile:
                        json.dump(events, outfile)

        return events


if __name__ == "__main__":
    EventsScraper(None).get_events()
