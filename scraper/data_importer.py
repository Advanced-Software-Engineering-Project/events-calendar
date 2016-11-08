import json
import sqlalchemy



url = 'postgresql://ase4156:dbpass@104.196.133.79/eventscalendar'
con = sqlalchemy.create_engine(url, client_encoding='utf8')
meta = sqlalchemy.MetaData(bind=con, reflect=True)

table = meta.tables['event']

json_data = open('scraper/data/events_data.json').read()
events = json.loads(json_data)

def do_import():
    for e in events:
        try:
            clause = table.insert().values(
                id          = e['id'],
                title       = e['title'],
                datetime    = e['datetime'],
                # group_id    = e['group_id'],
                group       = e['group'],
                group_url   = e['group_url'],
                # description = e['description'],
                location    = e['location'],
                photo_url   = e['photo_url']
            )
            con.execute(clause)

            print 'One event added. ID: {}'.format(e['id'])

        except Exception as e:
            print "Import Exception: {}".format(e)


if __name__ == "__main__":
    do_import()