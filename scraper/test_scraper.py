#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for Scraper module
Includes:
    Tests for Data Cleaner module
    Tests for Events Scraper module
    Tests for Data Importer module

@ase4156-backend: Ian
"""
#pylint: disable=E1101, E1120


# Code coverage start
from coverage import coverage
cov = coverage(branch=True, omit=['/Library/*',
                                  '/usr/local/lib/python2.7/site-packages/*',
                                  'scraper/test_scraper.py',
                                  'server/*'])
cov.start()
cov.exclude('pragma')


import json
import mock
import os

from datetime import datetime, timedelta
import unittest


from events_scraper import EventsScraper
from data_importer import DataImporter
from data_cleaner import DataCleaner

from server.app import db, app, Event, Group
from server import test_config


FILE_DIR = os.path.dirname(os.path.realpath('__file__'))
MOCK_EVENT_RESPONSE = os.path.join(FILE_DIR, 'scraper/mock_events_response.json')
data_file = open(MOCK_EVENT_RESPONSE)
mock_event_response = json.load(data_file)


# Mocking for Requests.get()
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

        assert response[0]['id'] == mock_event_response['data'][0]['id']
        assert response[0]['title'] == mock_event_response['data'][0]['name']
        assert response[0]['datetime'] == mock_event_response['data'][0]['start_time']
        assert response[0]['description'] == mock_event_response['data'][0]['description']
        assert response[0]['location'] == mock_event_response['data'][0]['place']['name']
        assert response[0]['photo_url'] == mock_event_response['data'][0]['cover']['source']
        # assert response[0]['group_id'] == mock_event_response['data'][0]['group_id']
        # assert response[0]['url'] == mock_event_response['data'][0]['datetime']

        assert len(response) > 0


class DataImporterTestCase(unittest.TestCase):
    '''
    Class for running test for the Data Importer
    '''

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.dataImporter = DataImporter(test_config.SQLALCHEMY_DATABASE_URI)

        self.app = app.test_client()
        return self.app

    def tearDown(self):
        db.drop_all()

    def test_import_groups_events(self):
        '''
        Test importing groups and events
        Must be run in same test as events have constraint to have associated group
        :return:
        '''
        response = self.dataImporter.import_groups('scraper/test_data/test_pages_data.json')
        assert response['imported_count'] == 6

        response = self.dataImporter.import_events('scraper/test_data/test_events_data.json')
        assert response['imported_count'] == 1


class DataCleanerTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.dataCleaner = DataCleaner(test_config.SQLALCHEMY_DATABASE_URI)

        self.app = app.test_client()
        return self.app

    def tearDown(self):
        db.drop_all()

    def test_delete_expired_events(self):
        # Add a group to test DB
        db.session.add(Group({
            'group_id': '456',
            'group': 'testgroup'
        }))
        db.session.commit()

        # Add two expired and one current event to test DB
        db.session.add(Event({
            'id': '123',
            'datetime': '1993-11-17T12:00:00',
            'location': 'mars',
            'group_id': '456',
            'title': 'a new event',
            'url': 'http://www.testevent.com',
            'photo_url': 'http://www.testphotourl.com'
        }))
        db.session.add(Event({
            'id': '124',
            'datetime': '1993-11-17T12:00:00',
            'location': 'mars',
            'group_id': '456',
            'title': 'a new event',
            'url': 'http://www.testevent.com',
            'photo_url': 'http://www.testphotourl.com'
        }))
        db.session.add(Event({
            'id': '125',
            'datetime': datetime.now() + timedelta(days = 2),
            'location': 'mars',
            'group_id': '456',
            'title': 'a new event',
            'url': 'http://www.testevent.com',
            'photo_url': 'http://www.testphotourl.com'
        }))
        db.session.commit()

        response = self.dataCleaner.do_clean()
        assert response['deleted_count'] == 2



if __name__ == "__main__":

    print 'here'
    try:
        unittest.main()
    except:
        pass

    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()

    cov.html_report(directory='scraper/coverage_report')
    cov.erase()

    print 'end'