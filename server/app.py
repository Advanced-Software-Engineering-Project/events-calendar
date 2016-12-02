#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
To run locally
    python server.py
Go to http://localhost:5000 in your browser

@ase4156-backend: Peng, Ian
"""
#pylint: disable=E1101, E1120
from datetime import datetime
import os
import time
import json
from functools import wraps, update_wrapper
import sqlalchemy
from flask import Flask, Response, request, jsonify, redirect, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin,\
                login_required, login_user, logout_user, current_user

app = Flask(__name__, static_url_path='', static_folder='../webapp/')


app.config.from_pyfile('config.py')
app.secret_key = 'super secret key'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

#%%

def nocache(view):
    """
    @nocache will clean cache after browing the page
    """
    @wraps(view)
    def no_cache(*args, **kwargs):
        """Rudimentary no cache"""
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, \
                                            must-revalidate, post-check=0, \
                                            pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    return update_wrapper(no_cache, view)


#%% <DATABASE SCHEMA>

#"""
#Table favorite(
#    user_id string FOREIGN KEY REFERENCES person(userid),
#    event_id string FOREIGN KEY REFERENCES event(eventid)
#)
#"""
favorite_table = \
    db.Table('favorite',
             db.Column('user_id', db.String(40), db.ForeignKey('person.id',  ondelete="CASCADE")),
             db.Column('event_id', db.String(40), db.ForeignKey('event.id',  ondelete="CASCADE"))
            )

rating_table = \
    db.Table('rating',
             db.Column('user_id', db.String(40), db.ForeignKey('person.id')),
             db.Column('group_id', db.String(40), db.ForeignKey('group.id')),
             db.Column('rate_value', db.Integer)
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
    favorites = db.relationship("Event", secondary=favorite_table, back_populates="fans", cascade="all, delete-orphan",
                    passive_deletes=True, single_parent=True)
                                # OPTIONALv0: child record delete on cascade
    groups_rated = db.relationship("Group", secondary=rating_table, back_populates="raters")

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

class Group(db.Model):
    """
    Table group(
    group_id char(40) PRIMARY KEY
    )
    """
    id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Float)
    raters = db.relationship("Person", secondary=rating_table, back_populates="groups_rated")

    def __init__(self, infodict):
        try:
            self.id = infodict['group_id']
            self.name = infodict['group']
            self.rating = 5.0
        except KeyError:
            print 'New event does not belong to any group.'
            self.id = '0'
            self.name = None
            self.rating = 0.0

    def __repr__(self):
        return "<GROUP {}, RATING {}>".format(self.id, self.rating)

class Event(db.Model):
    """
    Table event(
    id char(40) PRIMARY KEY
    )
    """
    id = db.Column(db.String(40), primary_key=True)
    datetime = db.Column(db.DateTime)
    location = db.Column(db.String(100))
    group_id = db.Column(db.String(40))
    title = db.Column(db.String(100))
    url = db.Column(db.Text)
    photo_url = db.Column(db.Text)
    fans = db.relationship("Person", secondary=favorite_table, back_populates="favorites", cascade="all, delete-orphan",
                    passive_deletes=True, single_parent=True)

    def __init__(self, infodict):
        self.id = infodict['id']
        try:
            self.datetime = infodict['datetime']
        except KeyError:
            self.datetime = None
        try:
            self.location = infodict['location']
        except KeyError:
            self.location = 'TBA'
        try:
            self.group_id = infodict['group_id']
        except KeyError:
            self.group_id = None
        try:
            self.title = infodict['title']
        except KeyError:
            self.title = 'Untitled Event'
        try:
            self.url = infodict['url']
        except KeyError:
            self.url = 'http://www.google.com'
        try:
            self.photo_url = infodict['photo_url']
        except KeyError:
            self.photo_url = None


    def __repr__(self):
        return "<{},{}>".format(self.id, self.title)

    def todict(self, bool_fav):
        """Output dictionary"""
        thegroup = Group.query.filter(Group.id == self.group_id).one()
        #print thegroup
        return {'id':self.id,
                'datetime':self.datetime.strftime("%Y-%m-%dT%H:%M:%S"),
                'location':self.location,
                'group_id':self.group_id,
                'title':self.title,
                'url':self.url,
                'photo_url':self.photo_url,
                'favorite': bool_fav,
                'group':thegroup.name,
                'rating':thegroup.rating,
                'popularity':len(self.fans)}

#%% <SERVER API>

@app.route('/mydeletetest')
def deleleachildrecord():
    events = Event.query.filter(Event.datetime < datetime.now()).all()
    theevent = events[0]
    print theevent.fans
    print theevent
    db.session.delete(theevent)
    db.session.commit()
    return 'Deleted a event record: \n{}\nON DELETE CASCADE WITH relationship'.format(theevent.title)


@login_manager.user_loader
def user_loader(id):
    """Core part of login_manager"""
    user = Person.query.filter(Person.id == id).one()
    return user


@app.route('/')
def root():
    """Index Page: Login"""
    return redirect('/login/index.html')


@app.route('/login/index.html')
@nocache
def cannotbeacurrentuser():
    """
    If a user is authenticated,
    login page will automatically
    redirect the user to the event page."""
    if not current_user.is_authenticated:
        return app.send_static_file('./login/index.html')
    else:
        return redirect('/events/index.html')


@app.route('/signup', methods=['POST'])
def signup():
    """sign up"""
    request_form = json.loads(request.data)

    if not 'email' in request_form:
        return Response('missing email', status=400)
    if not 'password' in request_form:
        return Response('missing password', status=400)
    if not 'firstname' in request_form:
        return Response('missing firstname', status=400)
    if not 'lastname' in request_form:
        return Response('missing lastname', status=400)

    new_user = Person(request_form['email'],
                      request_form['password'],
                      request_form['firstname'],
                      request_form['lastname'])
    db.session.add(new_user)

    try:
        db.session.commit()
        login_user(new_user)
        print 'Success: Sign up <{}>'.format(current_user.email)
        return jsonify(user_id=new_user.id)
    except sqlalchemy.exc.IntegrityError:
        print "Integrity Error: Conflict email address"
        db.session.rollback()
        response = jsonify(error='user exists')
        response.status_code = 409
        return response


@app.route('/login', methods=['POST'])
def login():
    """
    login:
    Every ip address allows to login a user as a current user
    """
    if request.method == 'POST':
        request_form = json.loads(request.data)
        res = Person.query.filter(Person.email == request_form['exist_email'],
                                  Person.password == request_form['exist_password']
                                 ).all()
        if len(res) != 0:
            login_user(res[0])
            print "Success: Login <{}>".format(current_user.email)
            return jsonify(user_id=current_user.id)
        else:
            print "Error: Invalid email-password combination"
            response = jsonify(error='invalid combination')
            response.status_code = 400
            return response


@app.route('/favorite', methods=['POST', 'DELETE'])
@login_required
def favorite_handler():
    """Post or delete a favorite event for current user"""
    request_form = json.loads(request.data)
    #print request_form
    event_id = str(request_form['id'])
    favone = Event.query.filter(Event.id == event_id).one()
    print 'Favorite_handler {}: {}'.format(request.method, favone)

    def favorite_exist(event_id):
        """Check if the event is current user's favorite"""
        cmd = """SELECT * FROM favorite WHERE user_id = :uid and event_id = :eid"""
        cursor = db.session.execute(cmd, dict(uid=current_user.id, eid=event_id))
        if cursor.fetchone() is None:
            cursor.close()
            return False
        cursor.close()
        return True

    if request.method == 'POST':
        # 409 for duplicate favorites
        if favorite_exist(favone.id):
            return Response('duplicate favorites', status=409)
        current_user.favorites.append(favone)
    elif request.method == 'DELETE':
        # 404 for delete nonexistant favorite
        if not favorite_exist(favone.id):
            return Response('nonexistant favorite', status=404)
        current_user.favorites.remove(favone)
    db.session.add(current_user)
    db.session.commit()
    return Response('success', status=200)


@app.route('/rate', methods=['POST'])
@login_required
def rate_group():
    """Current_user rate a group"""
    # Request the group_id and rate_value
    request_form = json.loads(request.data)
    # Check the rate_value
    try:
        if request_form['rate_value'] not in [1, 2, 3, 4, 5]:
            return Response('Error: invalid rate_value', status=400)
    except KeyError:
        return Response('Error: request rate_value', status=404)
    # Retrieve the group object
    thegroup = Group.query.filter(Group.id == request_form['group_id']).one()
    num_raters = len(thegroup.raters) + 1 #+1 for default 5 stars

    def rating_exist(group_id):
        """Check if the group has been rated by current user"""
        cmd = """SELECT * FROM rating WHERE user_id = :uid and group_id = :gid"""
        cursor = db.session.execute(cmd, dict(uid=current_user.id, gid=group_id))
        res = cursor.fetchone()
        if res is None:
            cursor.close()
            return False
        request_form['rate_value_old'] = res['rate_value']
        cursor.close()
        return True

    # If the current_user hasn't rated this group yet
    if not rating_exist(thegroup.id):
        # current_user becomes a rater of this group
        thegroup.raters.append(current_user)
        db.session.add(thegroup)
        db.session.commit()
        # store the rate_value
        cmd = """
              UPDATE rating 
              SET rate_value = :rate_value 
              WHERE user_id = :uid and group_id = :gid
              """
        db.session.execute(cmd, dict(uid=current_user.id,
                                     gid=thegroup.id,
                                     rate_value=int(request_form['rate_value'])
                                    ))
        db.session.commit()
        # update the rating of group
        thegroup.rating = (thegroup.rating * num_raters \
                           + request_form['rate_value'])*1.0 \
                           /(num_raters+1)
        db.session.commit()
    else: # the current_user has rated this group before
        # store the rate_value
        cmd = """
              UPDATE rating 
              SET rate_value = :rate_value 
              WHERE user_id = :uid and group_id = :gid
              """
        db.session.execute(cmd, dict(uid=current_user.id,
                                     gid=thegroup.id,
                                     rate_value=int(request_form['rate_value'])
                                    ))
        db.session.commit()
        # update the raing of group
        thegroup.rating = (thegroup.rating * num_raters - request_form['rate_value_old'] \
                           + request_form['rate_value'])*1.0 \
                           /num_raters
        db.session.commit()
    #print thegroup.rating
    return Response('success', status=200)


@app.route('/events/index.html', methods=['GET'])
@login_required
@nocache
def events_check():
    """A temp direction"""
    return app.send_static_file('./events/index.html')


@app.route('/events', methods=['GET'])
@login_required
@nocache
def events_handler():
    """Return info for main event page"""
    favbuf = current_user.favorites
    return jsonify(name=(current_user.firstname+' '+current_user.lastname),
                   email=current_user.email,
                   events=[o.todict(o in favbuf) for o in Event.query
                           .order_by(Event.datetime).all()])


@app.route('/logout', methods=['POST'])
def logout():
    """log out the current user for the ip sending this request"""
    if not current_user.is_authenticated:
        # 404 for duplicate logout
        return Response(status=404)
    logout_user()
    return redirect('/')

@login_manager.unauthorized_handler
def unauthorized_handler():
    """Unauthorized action"""
    return """
        <html>
          <meta http-equiv="refresh" content="3;url=/" />
          <h2>
            Not logged-in yet.<br><br>
            The page will automatically directs to index after 3 seconds...
          <h2>
        </html>
        """


#@app.route('/refresh/<int:count>')
#def refresh_event(count):
#    f = open('../scraper/data/events_data.json', 'r')
#    eventsdata = json.load(f)
#    f.close()
#    for i in range(0, count):
#        db.session.add(Event(eventsdata[i]))
#        try:
#            db.session.commit()
#            print 'One event added. ID:{}'.format(eventsdata[i]['id'])
#        except sqlalchemy.exc.IntegrityError:
#            print "Integrity Error: Event exists."
#            db.session.rollback()
#        #
#        db.session.add(Group(eventsdata[i]))
#        try:
#            db.session.commit()
#            print 'New group added. ID:{}'.format(eventsdata[i]['group_id'])
#        except sqlalchemy.exc.IntegrityError:
#            print "Integrity Error: Group exists."
#            db.session.rollback()
#    return redirect('login/index.html')



if __name__ == '__main__':
    db.create_all()
    print 'Database initialized.'

    import click

    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True) #RECOMMENDED
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=5000, type=int)
    def run(debug, threaded, host, port):
        """
        This function handles command line parameters.
        Run the server using
            python app.py
        Run the server with params using
            python app.py 127.0.0.1 8111 --threaded
        Show the help text using
            python app.py --help
        """

        # Note: prioirity for setting port:
        # 1. PORT environment variable (for Heroku)
        # 2. Command line argument
        # 3. Defaults to 5000
        env_port = int(os.environ.get("PORT", port))

        HOST, PORT = host, env_port

        print "running on %s:%d" % (HOST, PORT)
        app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

    run()
