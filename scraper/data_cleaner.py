import sqlalchemy
from datetime import datetime

from server.app import Event

url = 'postgresql://ase4156:dbpass@104.196.133.79/eventscalendar'
con = sqlalchemy.create_engine(url, client_encoding='utf8')
meta = sqlalchemy.MetaData(bind=con, reflect=True)

events_table = meta.tables['event']

'''
Delete past events from our DB
'''
def do_clean():
    try:
        time = datetime.now()

        clause = events_table.delete(Event.datetime < time)
        con.execute(clause)

        print 'Deleted old events'

    except Exception as e:
        print "Import Exception: {}".format(e)


if __name__ == "__main__":
    do_clean()
