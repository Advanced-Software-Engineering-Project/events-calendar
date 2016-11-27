import json
import sqlalchemy



url = 'postgresql://ase4156:dbpass@104.196.133.79/eventscalendar'
con = sqlalchemy.create_engine(url, client_encoding='utf8')
meta = sqlalchemy.MetaData(bind=con, reflect=True)

events_table = meta.tables['event']
groups_table = meta.tables['group']

json_data = open('scraper/data/events_data.json').read()
events = json.loads(json_data)

def import_events():
    for e in events:
        try:
            clause = events_table.insert().values(
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


def import_groups():
    groups_json = open('scraper/data/pages_data.json').read()

    for g in groups_json:
        try:
            clause = groups_table.insert().values(
                id = g['id'],
                name = g['group_name'],
                group_url = g['group_url'],
            )
            con.execute(clause)

            print 'One event added. ID: {}'.format(g['id'])

        except Exception as e:
            print "Import Exception: {}".format(e)



if __name__ == "__main__":
    import_events()