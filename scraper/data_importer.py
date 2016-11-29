#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for importing Columbia events from Json file
"""
#pylint: disable=E1101, E1120

import json
import sqlalchemy

from server import config


URL = config.SQLALCHEMY_DATABASE_URI
CON = sqlalchemy.create_engine(URL, client_encoding='utf8')
META = sqlalchemy.MetaData(bind=CON, reflect=True)

EVENTS_TABLE = META.tables['event']
GROUPS_TABLE = META.tables['group']


# id = db.Column(db.String(40), primary_key=True)
# datetime = db.Column(db.DateTime)
# location = db.Column(db.String(100))
# group_id = db.Column(db.String(40))
# title = db.Column(db.String(100))
# url = db.Column(db.Text)
# photo_url = db.Column(db.Text)
def import_events():
    """
    Use data/events_data.json file to import Columbia groups data into db
    :return:
    """
    data_file = open('scraper/data/events_data.json').read()
    events_json = json.loads(data_file)

    for event in events_json:
        try:
            clause = EVENTS_TABLE.insert().values(
                id=event['id'],
                datetime=event['datetime'],
                location=event['location'],
                group_id=event['group_id'],
                title=event['title'],
                url=event['url'],
                photo_url=event['photo_url']
                # description = e['description'],
            )
            CON.execute(clause)

            print 'One event added. ID: {}'.format(event['id'])

        except Exception as error:
            print "Import Exception: {}".format(error)


# id = db.Column(db.String(40), primary_key=True)
# name = db.Column(db.String(100))
# rating = db.Column(db.Float)
def import_groups():
    """
    Use data/pages_data.json file to import Columbia groups data into db
    :return:
    """
    data_file = open('scraper/data/pages_data.json', 'r')
    groups_json = json.load(data_file)

    for group in groups_json:
        try:
            clause = GROUPS_TABLE.insert().values(
                id=str(group['group_id']),
                name=group['group_name'],
                rating=5.0
                # group_url   = e['group_url'],
            )
            CON.execute(clause)

            print 'One event added. ID: {}'.format(group['id'])

        except Exception as error:
            print "Import Exception: {}".format(error)


if __name__ == "__main__":
    import_groups()
    import_events()
