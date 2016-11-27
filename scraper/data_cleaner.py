import sqlalchemy
from datetime import datetime

from server.app import Event

url = 'postgresql://ase4156:dbpass@104.196.133.79/eventscalendar'
con = sqlalchemy.create_engine(url, client_encoding='utf8')
meta = sqlalchemy.MetaData(bind=con, reflect=True)

table = meta.tables['event']

def do_clean():
    try:
        time = datetime.now()
        # todo - create new field for 'expired' instead of deleting
        table.query(Event).filter(Event.datetime < time).delete()

        print 'Deleted old events'

    except Exception as e:
        print "Import Exception: {}".format(e)


if __name__ == "__main__":
    do_clean()