import unittest
import json
from datetime import datetime

from app import db, app, Person, Event, Group

from unittest.mock import MagicMock

from server import config

import events_scraper


class EventsScraperTestCase(unittest.TestCase):

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

    def test_scrape_events(self):


        response = data_cleaner.do_clean()
        assert response.deleted_count == 2
