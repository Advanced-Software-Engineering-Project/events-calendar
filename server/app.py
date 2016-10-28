#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
To run locally
    python server.py
Go to http://localhost:5000 in your browser

@author: peng
"""
from datetime import datetime
import os
import time
import json
import sqlalchemy
from flask import Flask, Response, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='../webapp/')
            #template_folder='../webapp/')
app.config.from_pyfile('config.py')
app.secret_key = 'super secret key'
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
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    username = db.Column(db.String(80), unique=True)    
    created_at = db.Column(db.DateTime)

    def __init__(self, email, password, firstname, lastname):
        self.userid = "{}".format(int(time.time() * 1000))
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.username = None
        self.created_at = datetime.now()

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
db.create_all()

#app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))
    
@app.route('/signup', methods=['POST'])
def signup():
    request_form = json.loads(request.data)    
    new_user = Person(request_form['email'], 
                      request_form['password'], 
                      request_form['firstname'],
                      request_form['lastname'])    
    db.session.add(new_user)
    try:
        db.session.commit()
        print 'You were successfully signed up.'
        return jsonify(user_id=new_user.userid)
    except sqlalchemy.exc.IntegrityError:
        print "Integrity Error: Conflict email address!!!"
        db.session.rollback()
        return "Signup Error"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print "#######\nHere I am\n#######"
        request_form = json.loads(request.data)
        res = Person.query.filter(Person.email == request_form['exist_email'],
                                  Person.password == request_form['exist_password']
                                  ).all()
        if len(res)!= 0:
            #session['logged_in']=True
            print "Login successfully."
            return jsonify(user_id=res[0].userid)
            #return redirect(url_for('events_handler'))
        else:
            print "Invalid email-password combination."
            return "Login Error"   


@app.route('/eventss', methods=['GET'])
def events_handler():
    	events = [{
	    'id': '1009214592509511',
	    'datetime': '2016-02-25T19:00:00-0500',
	    'location': 'Fairchild 700',
	    'group': 'Columbia Bioinformatics',
	    'title': 'Bioinformatics Student Research Panel',
	    'url': 'https://www.facebook.com/events/563717810449699/',
	    'rating': 3,
	    'favorite': 1
	}, {
	    'id': '1009214592509511',
	    'datetime': '2016-02-25T19:00:00-0500',
	    'location': 'Fairchild 700',
	    'group': 'Columbia Bioinformatics',
	    'title': 'Bioinformatics Student Research Panel',
	    'url': 'https://www.facebook.com/events/563717810449699/',
	    'rating': 5,
	    'favorite': 0
	}]
	print(request)
	return jsonify(events=events)
#    if request.method == 'POST':
#        new_event = dict([('eventid','#facebook123'), ('title', 'Ballroom Dance')])
#        db.session.add(Event(new_event['eventid'], new_event['title']))
#        db.session.commit()
#        return 'New event posted'
#    else:
#        print "##############"
#        print request.data
#        return Event.query.all()

        
##Temporary local development solution for CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)
