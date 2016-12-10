#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for Events Scraper module

@ase4156-backend: Ian
"""
#pylint: disable=E1101, E1120


import json
import mock
import os
import unittest

from server.app import db, app

from events_scraper import EventsScraper


FILE_DIR = os.path.dirname(os.path.realpath('__file__'))
MOCK_EVENT_RESPONSE = os.path.join(FILE_DIR, 'scraper/mock_events_response.json')
data_file = open(MOCK_EVENT_RESPONSE)
mock_event_response = json.load(data_file)


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse(mock_event_response, 200)


class EventsScraperTestCase(unittest.TestCase):
    '''
    Class for running tests related to the Events Scraper
    '''

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.app = app.test_client()
        self.eventsScraper = EventsScraper('scraper/test_data/test_pages_data.json')

        return self.app

    def tearDown(self):
        db.drop_all()

    @mock.patch('requests.get', mock.Mock(side_effect = mocked_requests_get))
    def test_scrape_events(self):
        response = self.eventsScraper.get_events()

        assert response[0]['datetime'] == mock_event_response['data'][0]['start_time']
        assert response[0]['description'] == mock_event_response['data'][0]['description']
        assert response[0]['id'] == mock_event_response['data'][0]['id']
        # assert response[0]['group_id'] == mock_event_response['data'][0]['group_id']
        assert response[0]['location'] == mock_event_response['data'][0]['place']['name']
        assert response[0]['photo_url'] == mock_event_response['data'][0]['cover']['source']
        assert response[0]['title'] == mock_event_response['data'][0]['name']
        # assert response[0]['url'] == mock_event_response['data'][0]['datetime']

        assert len(response) != 0
