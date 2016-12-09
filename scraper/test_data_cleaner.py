import unittest
import json
from datetime import datetime

from app import db, app, Person, Event, Group

from server import config

import data_cleaner


class DataCleanerTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.app = app.test_client()

        # Create test user
        new_user = Person(
            'validuser@columbia.edu',
            'validpassword',
            'test',
            'testerson'
        )
        db.session.add(new_user)
        db.session.commit()

        return self.app

    def tearDown(self):
        db.drop_all()

    def test_delete_expired_events(self):
        # Add a group to test DB
        db.session.add(Group({
            'group_id': '456',
            'group': 'testgroup'
        }))

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
            'id': '123',
            'datetime': '1993-11-17T12:00:00',
            'location': 'mars',
            'group_id': '456',
            'title': 'a new event',
            'url': 'http://www.testevent.com',
            'photo_url': 'http://www.testphotourl.com'
        }))
        db.session.add(Event({
            'id': '123',
            'datetime': datetime.now(),
            'location': 'mars',
            'group_id': '456',
            'title': 'a new event',
            'url': 'http://www.testevent.com',
            'photo_url': 'http://www.testphotourl.com'
        }))
        db.session.commit()

        response = data_cleaner.do_clean()
        assert response.deleted_count == 2
