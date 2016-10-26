# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:31:56 2016

@author: peng
"""
from datetime import datetime
import os
import time

from flask import Flask, Response, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='../webapp/login/')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

#%% <DATABASE SCHEMA>
"""
CODE SECTION: DATABASE SCHEMA
IN USE: Person, Event
"""

#Favorite = db.Table('Favorite',
#    db.Column('userid', db.Integer, db.ForeignKey('Person.userid')),
#    db.Column('eventid', db.Text, db.ForeignKey('Event.eventid'))
#    )
"""
Table favorite(
userid int FOREIGN KEY REFERENCES person(userid),
eventid text FOREIGN KEY REFERENCES event(eventid)
)
"""

class Person(db.Model):
    """
    TABLE person(
    userid varchar(40) PRIMARY KEY,
    email varchar(120) UNIQUE NOT NULL,
    password varchar(80) NOT NULL,
    username varchar(80) UNIQUE
    )
    """
    userid = db.Column(db.String(40), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True)
    created_at = db.Column(db.DateTime)

    def __init__(self, userid, email, password, created_at):
        self.userid = userid
        self.email = email
        self.password = password
        self.username = None
        self.created_at = created_at

    def __repr__(self):
        return '<User %r>' % self.email

class Event(db.Model):
    """
    Table event(
    eventid text PRIMARY KEY,
    eventdate date,
    location text,
    group text,
    title text NOT NULL,    
    url text,
    rating float,
    )
    """
    eventid = db.Column(db.Text, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    rate = db.Column(db.Float)
        
    def __init__(self, eventid, title):
        self.eventid = eventid
        self.title = title
    
    def __repr__(self):
        return "{},{},{}".format(self.eventid, self.title, self.rate)
        
    def update_rating(self, newrate):
        pass

#class Rate(db.Model):
    """
    Table rate(
    userid int FOREIGN KEY REFERENCES person(userid),
    eventid text FOREIGN KEY REFERENCES event(eventid),
    rate int,
    CHECK (rate in (1,2,3,4,5))
    )
    """
    

#%% <SERVER API>
"""
CODE SECTION: SERVER API
IN USE: signup, login, calendar
"""

@app.route('/')
def hello():
    return "Hello Index!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
@app.route('/signup')
def signup(email, password):
    #data = request.form.to_dict()
    not_signed = Person.query.filter(Person.email == email).one_or_none() == None
    if not_signed:
        db.create_all()
        new_id = "{}".format(int(time.time() * 1000))
        new_user = Person(new_id, email, password, datetime.now())
        db.session.add(new_user)
        db.session.commit()
        print "Signed up successfully."
        return "userid:{}".format(new_id)
    else:
        print "The email address has been used."
        return "Signup error"

@app.route('/login')
def login(email, password):
    res = Person.query.filter(Person.email == email,
                        Person.password == password).all()
    if len(res)!= 0:
        print "Login successfully."
        return "{}".format(res[0].userid)
    else:
        print "Wrong email-password combination."
        return "Login Error"
        

@app.route('/calendar', methods=['POST', 'OPTIONS'])
def event_handler(request_method):
    #if request.method == 'POST':
    if request_method == 'POST':
        db.create_all()
        new_event = dict([('eventid','#facebook123'), ('title', 'Ballroom Dance')])
        db.session.add(Event(new_event['eventid'], new_event['title']))
        db.session.commit()
        return 'New event posted'
    else:
        return Event.query.all()
        
# Temporary local development solution for CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)