#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for clearing past events from our database
"""
# pylint: disable=E1101, E1120

from datetime import datetime
import sqlalchemy

from server import config, app


class DataCleaner:

    def __init__(self, test_db_url):
        url = config.SQLALCHEMY_DATABASE_URI

        # For testing
        if test_db_url:
            url = test_db_url

        self.connection = sqlalchemy.create_engine(url, client_encoding='utf8')
        meta = sqlalchemy.MetaData(bind=self.connection, reflect=True)

        self.EVENTS_TABLE = meta.tables['event']

    def do_clean(self):
        """
        Delete events older than today from our DB
        :return:
        """
        deleted_count = 0
        try:
            now_time = datetime.now()
            stmt = self.EVENTS_TABLE.delete(app.Event.datetime < now_time)
            result = self.connection.execute(stmt)

            deleted_count = result.rowcount
            print 'Deleted <' + str(result.rowcount) + '> old events'

        except Exception as error:
            print "Import Exception: {}".format(error)

        return {'deleted_count': deleted_count}


if __name__ == "__main__":
    DataCleaner(None).do_clean()
