#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for Data Cleaner module

@ase4156-backend: Ian
"""
#pylint: disable=E1101, E1120

from datetime import datetime, timedelta
import unittest

from data_cleaner import DataCleaner
from server.app import db, app, Event, Group
from server import test_config



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
