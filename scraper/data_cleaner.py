#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module for clearing past events from our database
"""
#pylint: disable=E1101, E1120

from datetime import datetime
import sqlalchemy

from server.app import Event
from server import config


URL = config.SQLALCHEMY_DATABASE_URI
CON = sqlalchemy.create_engine(URL, client_encoding='utf8')
META = sqlalchemy.MetaData(bind=CON, reflect=True)

EVENTS_TABLE = META.tables['event']

def do_clean():
    """
    Delete events older than today from our DB
    :return:
    """
    try:
        now_time = datetime.now()
        stmt = EVENTS_TABLE.delete(Event.datetime < now_time)
        result = CON.execute(stmt)

        print 'Deleted <' + str(result.rowcount) + '> old events'

    except Exception as error:
        print "Import Exception: {}".format(error)


if __name__ == "__main__":
    do_clean()
