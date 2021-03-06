#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for importing Columbia events from Json file
"""
# pylint: disable=E1101, E1120

import json
import sqlalchemy

from server import config


class DataImporter:
    """
    Class in charge of doing imports from files generated by the events scraper
    Imports Groups from groups file
    Imports Events from events file
    """

    def __init__(self, test_db_url):
        url = config.SQLALCHEMY_DATABASE_URI
        # For testing
        if test_db_url:
            url = test_db_url

        self.connection = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=self.connection, reflect=True)

        self.events_table = meta.tables['event']
        self.groups_table = meta.tables['group']

    # id = db.Column(db.String(40), primary_key=True)
    # datetime = db.Column(db.DateTime)
    # location = db.Column(db.String(100))
    # group_id = db.Column(db.String(40))
    # title = db.Column(db.String(100))
    # url = db.Column(db.Text)
    # photo_url = db.Column(db.Text)
    def import_events(self, events_file):
        """
        Use data/events_data.json file to import Columbia groups data into db
        :return:
        """
        data_file = open(events_file).read()
        events_json = json.loads(data_file)

        imported_count = 0
        for event in events_json:
            try:
                clause = self.events_table.insert().values(
                    id=event['id'],
                    datetime=event['datetime'],
                    location=event['location'],
                    group_id=event['group_id'],
                    title=event['title'],
                    url=event['url'],
                    photo_url=event['photo_url']
                    # description = e['description'],
                )
                self.connection.execute(clause)

                print 'One event added. ID: {}'.format(event['id'])
                imported_count += 1

            except Exception as error:
                print "Import Exception: {}".format(error)

        print "Imported <{}> events".format(imported_count)
        return {'imported_count': imported_count}

    # id = db.Column(db.String(40), primary_key=True)
    # name = db.Column(db.String(100))
    # rating = db.Column(db.Float)
    def import_groups(self, groups_file):
        """
        Use data/pages_data.json file to import Columbia groups data into db
        :return:
        """
        data_file = open(groups_file, 'r')
        groups_json = json.load(data_file)

        imported_count = 0
        for group in groups_json:
            try:
                clause = self.groups_table.insert().values(
                    id=str(group['group_id']),
                    name=group['group_name'],
                    rating=5.0
                    # group_url   = e['group_url'],
                )
                self.connection.execute(clause)

                print 'One group added. ID: {}'.format(group['group_id'])
                imported_count += 1

            except Exception as error:
                print "Import Exception: {}".format(error)

        print "Imported <{}> groups".format(imported_count)
        return {'imported_count': imported_count}


if __name__ == "__main__":
    dataImporter = DataImporter(None)
    dataImporter.import_groups('scraper/data/pages_data_3.json')
    dataImporter.import_events('scraper/data/events_data.json')
