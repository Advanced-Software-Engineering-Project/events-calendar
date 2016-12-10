#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for Data Importer module

@ase4156-backend: Ian
"""
#pylint: disable=E1101, E1120

import unittest

from data_importer import DataImporter
from server.app import db, app
from server import test_config


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
