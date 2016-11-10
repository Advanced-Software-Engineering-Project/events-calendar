# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:47:36 2016

@author: peng
"""


<<<<<<< HEAD
from flask import Flask
=======
>>>>>>> 40257ad0a69f261c746378b2035b235428434f1f
import unittest
import json

from app import db, app, refresh_event
<<<<<<< Updated upstream

=======

<<<<<<< HEAD

#from app.models import User
=======
>>>>>>> origin/master
>>>>>>> Stashed changes

class SignupTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        print "### Testing Starts ###"
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.app = app.test_client()
        return self.app


    def tearDown(self):
        db.drop_all()

    def test_user_signup(self):
        response = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))
        assert response.status_code == 201
    def test_user_bademail(self):
        response = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))
        assert response.status_code == 400
    def test_exist(self):
        response = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))
        assert response.status_code == 409                




class LoginTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.app = app.test_client()
        return self.app


    def tearDown(self):
        db.drop_all()
        


    def test_user_login(self):
        response = self.app.post('/login', data = json.dumps(dict(
            exist_email='abc@columbia.edu',
            exist_password='passwd'
        )))
        assert response.status_code == 200
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    
    def test_invalid(self):
        response = self.app.post('/login', data = json.dumps(dict(
            exist_email='abc@columbia.edu',
            exist_password='wrongpassword'
        )))
        assert response.status_code == 401

class FavoritesTestCase(unittest.TestCase):

    def setUp(self):
        #Creates a new database for the unit test to use
    
=======
>>>>>>> Stashed changes

















class EventsTestCase(unittest.TestCase):


    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
        self.app = app.test_client()

        user = User(active=True)
        db.session.add(user)
        db.session.commit()
        login_user(user)


    def tearDown(self):
        db.drop_all()

    def easylogin():
=======
>>>>>>> Stashed changes
        app.config['TESTING'] = True
        app.login_manager.init_app(app)

        self.app = app.test_client()

        self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))

<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes
        self.app.post('/login', data = json.dumps(dict(
            exist_email='abc@columbia.edu',
            exist_password='passwd'
        )))

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    def test_set_favorites(self):
        easylogin()
        response = self.app.post('/favorite', data = json.dumps(dict(id = '')
        ))
        print(response)
        assert response.status_code == 201
    def test_unset_favorites(self):
        response = self.app.delete('/favorite', data = json.dumps(dict(
            exist_email='abc@columbia.edu',
            exist_password='passwd'
        )))
        print(response)
        assert response.status_code == 200
    def show_favorites(self):
        response = self.app.post('/favorite', data = json.dumps(dict(
            exist_email='abc@columbia.edu',
            exist_password='passwd'
        )))
        print(response)
        assert response.status_code == 200
        
=======
>>>>>>> Stashed changes

    def tearDown(self):
        db.drop_all()


    def test_no_events(self):
        response = self.app.get('/events',
            content_type='application/json'
        )
        data = json.loads(response.data)
        assert len(data['events']) == 0


    def test_events_returned(self):
        # Add some events to test DB
        refresh_event(2)

        response = self.app.get('/events',
            content_type='application/json'
        )
        data = json.loads(response.data)
        assert len(data['events']) == 2






<<<<<<< Updated upstream
=======
>>>>>>> origin/master
>>>>>>> Stashed changes

if __name__ == '__main__':
    unittest.main()
