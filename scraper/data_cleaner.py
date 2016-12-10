#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for clearing past events from our database
"""
#pylint: disable=E1101, E1120

from datetime import datetime
import sqlalchemy

# from server.app import Event
from server import config, app



class DataCleaner():

    def __init__(self, test_db_url):
        URL = config.SQLALCHEMY_DATABASE_URI

        # For testing
        if test_db_url:
            URL = test_db_url

        self.CON = sqlalchemy.create_engine(URL, client_encoding='utf8')
        META = sqlalchemy.MetaData(bind=self.CON, reflect=True)

        self.EVENTS_TABLE = META.tables['event']

    def do_clean(self):
        """
        Delete events older than today from our DB
        :return:
        """
        deleted_count = 0
        try:
            now_time = datetime.now()
            stmt = self.EVENTS_TABLE.delete(app.Event.datetime < now_time)
            result = self.CON.execute(stmt)

            deleted_count = result.rowcount
            print 'Deleted <' + str(result.rowcount) + '> old events'

        except Exception as error:
            print "Import Exception: {}".format(error)

        return {'deleted_count': deleted_count}


if __name__ == "__main__":
    DataCleaner(None).do_clean()
