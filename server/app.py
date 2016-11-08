#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
To run locally
    python server.py
Go to http://localhost:5000 in your browser

@ase4156-backend: Peng, Ian
"""
from datetime import datetime
import os
import time
import json
import sqlalchemy
from flask import Flask, Response, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin,\
                login_required, login_user, logout_user, current_user

app = Flask(__name__, static_url_path='', static_folder='../webapp/')
app.config.from_pyfile('config.py')
app.secret_key = 'super secret key'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

#%% <DATABASE SCHEMA>
"""
CODE SECTION: DATABASE SCHEMA
IN USE: Person, Event
"""


"""
Table favorite(
    user_id string FOREIGN KEY REFERENCES person(userid),
    event_id string FOREIGN KEY REFERENCES event(eventid)
)
"""
favorite_table = db.Table('favorite',
    db.Column('user_id', db.String(40), db.ForeignKey('person.id')),
    db.Column('event_id', db.String(40), db.ForeignKey('event.id'))
    )

class Person(db.Model, UserMixin):
    """
    TABLE person(
    id varchar(40) PRIMARY KEY
    )
    """
    id = db.Column(db.String(40), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    username = db.Column(db.String(80), unique=True)
    created_at = db.Column(db.DateTime)
    favorites = db.relationship("Event", secondary = favorite_table,\
				# OPTIONALv0: child record delete on cascade
				back_populates = "fans")

    def __init__(self, email, password, firstname, lastname):
        self.id = "{}".format(int(time.time() * 1000))
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
    id text PRIMARY KEY
    )
    """
    id = db.Column(db.String(40), primary_key=True)
    datetime = db.Column(db.String(30))
    location = db.Column(db.String(100))
    group = db.Column(db.String(100))
    title = db.Column(db.String(100))
    group_url = db.Column(db.Text)
    photo_url = db.Column(db.Text)
    rating = db.Column(db.Integer)
    fans = db.relationship("Person", secondary = favorite_table, back_populates="favorites")

    def __init__(self, infodict):
        self.id = infodict['id']
        try:
            self.datetime = infodict['datetime']
        except:
            self.datetime = None
        try:
            self.location = infodict['location']
        except:
            self.location = None
        try:
            self.group = infodict['group']
        except:
            self.group = None
        try:
            self.title = infodict['title']
        except:
            self.title = 'Untitled Event'
        try:
            self.group_url = infodict['group_url']
        except:
            self.group_url = None
        try:
            self.photo_url = infodict['photo_url']
        except:
            self.photo_url = None
        try:
            self.rating = infodict['rating']
        except:
            self.rating = 4

    def __repr__(self):
        return "<{},{}>".format(self.id, self.title)

    def todict(self, bool_fav):
        """ Output dictionary """
        return {'id':self.id,
                'datetime':self.datetime,
                'location':self.location,
                'group':self.group,
                'title':self.title,
                'group_url':self.group_url,
                'photo_url':self.photo_url,
                'rating':self.rating,
                'favorite': bool_fav
               }

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
# def init_db():
db.create_all()
print 'Database initialized'

@login_manager.user_loader
def user_loader(id):
    user = Person.query.filter(Person.id == id).one()
    return user

@app.route('/')
def root():
    return redirect('/login/index.html')

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
        login_user(new_user)
        return jsonify(user_id=new_user.id)
    except sqlalchemy.exc.IntegrityError:
        print "Integrity Error: Conflict email address!!!"
        db.session.rollback()
        response = jsonify({'error': 'user exists'})
        response.status_code = 400
        return response

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        request_form = json.loads(request.data)
        res = Person.query.filter(Person.email == request_form['exist_email'],
                                  Person.password == request_form['exist_password']
                                 ).all()
        if len(res) != 0:
            login_user(res[0])
            print "Login successfully:", current_user
            #return redirect('/events/index.html')
            return jsonify(user_id=current_user.id)
        else:
            print "Invalid email-password combination."
            response = jsonify({'error': 'invalid combination'})
            response.status_code = 400
            return response

@app.route("/get_userid")
@login_required
def get_uid():
    return jsonify(user_id=current_user.id)

@app.route("/protected", methods=["GET"])
@login_required
def protected():
    return Response(response="{}:Hello Protected World!".format(current_user.email), status=200)

@app.route('/favorite', methods=['POST', 'DELETE'])
def addtorelationship():
    request_form = json.loads(request.data)
    print request_form
    event_id = str(request_form['id'])
    favone = Event.query.filter(Event.id == event_id).one()
    print favone
    if request.method == 'POST':
        current_user.favorites.append(favone)
    elif request.method == 'DELETE':
        current_user.favorites.remove(favone)
    db.session.add(current_user)
    db.session.commit()
    return Response('success')

@app.route('/events/index.html')
@login_required
def events_check():
    return app.send_static_file('./events/index.html')

@app.route('/events', methods=['GET'])
@login_required
def events_handler():
    favbuf = current_user.favorites
    print favbuf
    print '###'
    #print [o.todict(o in favbuf) for o in Event.query.all()]    
    return jsonify(events=[o.todict(o in favbuf) for o in Event.query.all()])

@app.route('/logout')
def logout():
    logout_user()
    return Response()

@login_manager.unauthorized_handler
def unauthorized_handler():
    print 'Unauthorized action'
    return redirect('/')

@app.route('/refresh')
def refresh_event():
#    eventsdata = [{
#	    'id': '1009214592509511',
#	    'datetime': '2016-02-25T19:00:00-0500',
#	    'location': 'Fairchild 700',
#	    'group': 'Columbia Bioinformatics',
#	    'title': 'Bioinformatics Student Research Panel',
#	    'url': 'https://www.facebook.com/events/563717810449699/',
#	    'rating': 3,
#	    'favorite': 1
#     }, {
#	    'id': '1009214592509512',
#	    'datetime': '2016-02-25T19:00:00-0500',
#	    'location': 'Fairchild 700',
#	    'group': 'Columbia Bioinformatics',
#	    'title': 'Bioinformatics Student Research Panel',
#	    'url': 'https://www.facebook.com/events/563717810449699/',
#	    'rating': 5,
#	    'favorite': 0
#	}]
    f = open('../scraper/data/events_data.json', 'r')
    eventsdata = json.load(f)
    f.close()
    for i in range(0, 20):
        db.session.add(Event(eventsdata[i]))
        try:
            db.session.commit()
            print 'One event added. ID:{}'.format(eventsdata[i]['id'])
        except sqlalchemy.exc.IntegrityError:
            print "Integrity Error: old event."
            db.session.rollback()
    #print '###########'
    #print [o.__dict__ for o in Event.query.all()]
    #print [o.todict() for o in Event.query.all()]
    return redirect('login/index.html')


if __name__ == '__main__':
    import click
    
    env_port = int(os.environ.get("PORT", 5000))
 
    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)#RECOMMENDED
    #@click.argument('HOST', default='0.0.0.0')
    @click.argument('HOST', default='127.0.0.1')
    @click.argument('PORT', default=env_port, type=int)
    def run(debug, threaded, host, port):
      """
      This function handles command line parameters.
      Run the server using
          python server.py
      Show the help text using
          python server.py --help
      """
  
      HOST, PORT = host, port
      print "running on %s:%d" % (HOST, PORT)
      app.run(host=HOST, port=env_port, debug=debug, threaded=threaded)
  
  
    run()
