from datetime import datetime
import sqlalchemy
from sqlalchemy import delete
from datetime import datetime

from server.app import Event
from server import config

url = config.SQLALCHEMY_DATABASE_URI
con = sqlalchemy.create_engine(url, client_encoding='utf8')
meta = sqlalchemy.MetaData(bind=con, reflect=True)

events_table = meta.tables['event']

'''
Delete past events from our DB
'''
def do_clean():
    try:
        now_time = datetime.now()
        stmt = events_table.delete(Event.datetime < now_time)
        result = con.execute(stmt)
        
        print 'Deleted <' + str(result.rowcount) + '> old events'

    except Exception as e:
        print "Import Exception: {}".format(e)


if __name__ == "__main__":
    do_clean()
