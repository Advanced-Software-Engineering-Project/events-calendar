# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 23:11:32 2016

@author: peng
"""
#%% <READ CSV>
file_path = '../scraper/data/events_data.csv'

def load_data():
    """
    This method reads the dataset, and returns a list of rows.
    Each row is a list containing the values in each column.
    """
    import csv
    with open(file_path) as f:
        f.seek(0)
        #reader = csv.reader(f)
        reader = csv.DictReader(f)
        return [l for l in reader]

data = load_data()


#%% <POUR INTO SQL>

import sqlalchemy
print sqlalchemy.__version__

from sqlalchemy import create_engine
engine = create_engine("postgresql://ase4156:dbpass@localhost/eventscalendar", echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text, DateTime, Float
class Event(Base):
    __tablename__ = 'events'

    id = Column(String(40), primary_key=True)
    datetime = Column(DateTime)
    title = Column(String(120))
    description = Column(Text)
    location = Column(String(120))
    group = Column(String(120))
    url = Column(Text)
    #rating = Column(Float)
        
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)
    
#    def todict(self):
#        return {"id":self.id, "name": self.name, "fullname": self.fullname} 
            
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

new_event = Event(id = data[0]['id'])
session.add(new_event)
try:
    session.commit()
except sqlalchemy.exc.IntegrityError:
    print "Integrity Error!!!!!!!!!!!!"
    session.rollback()

#print '############'
#from sqlalchemy import text
#result = session.query(Event).from_statement(
#    text("SELECT * FROM users where name=:name")).\
#    params(name='ed').all()
#print result
#print result[0].todict()
session.close()