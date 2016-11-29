import json
import sqlalchemy

from server import config


url = config.SQLALCHEMY_DATABASE_URI
con = sqlalchemy.create_engine(url, client_encoding='utf8')
meta = sqlalchemy.MetaData(bind=con, reflect=True)

events_table = meta.tables['event']
groups_table = meta.tables['group']

json_data = open('scraper/data/events_data.json').read()
events = json.loads(json_data)



# id = db.Column(db.String(40), primary_key=True)
# datetime = db.Column(db.DateTime)
# location = db.Column(db.String(100))
# group_id = db.Column(db.String(40))
# title = db.Column(db.String(100))
# url = db.Column(db.Text)
# photo_url = db.Column(db.Text)
def import_events():
    for e in events:
        try:
            clause = events_table.insert().values(
                id          = e['id'],
                datetime    = e['datetime'],
                location    = e['location'],
                group_id    = e['group_id'],
                title       = e['title'],
                url         = e['url'],
                photo_url   = e['photo_url']
                # description = e['description'],
            )
            con.execute(clause)

            print 'One event added. ID: {}'.format(e['id'])

        except Exception as e:
            print "Import Exception: {}".format(e)


# id = db.Column(db.String(40), primary_key=True)
# name = db.Column(db.String(100))
# rating = db.Column(db.Float)
def import_groups():
    f = open('scraper/data/pages_data.json', 'r')
    groups_json = json.load(f)

    for g in groups_json:
        try:
            clause = groups_table.insert().values(
                id          = str(g['group_id']),
                name        = g['group_name'],
                rating      = 5.0
                # group_url   = e['group_url'],
            )
            con.execute(clause)

            print 'One event added. ID: {}'.format(g['id'])

        except Exception as e:
            print "Import Exception: {}".format(e)



if __name__ == "__main__":
    import_groups()
    import_events()
