# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:47:36 2016

@author: peng
"""

import unittest
import json

from app import db, app, Person, Event


class SignupTestCase(unittest.TestCase):

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

    def test_user_signup(self):
        response = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))
        assert response.status_code == 200

    def test_exist(self):
        self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))
        # Duplicate accounts
        response = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))

        assert response.status_code == 409

    def test_incomplete_data(self):
        '''
        Missing email, password, firstname, lastname
        '''
        resp = self.app.post('/signup', data = json.dumps(dict(
            password='passwd',
            firstname='cd',
            lastname='ab'
        )))
        assert resp.status_code == 400

        resp = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            firstname='cd',
            lastname='ab'
        )))
        assert resp.status_code == 400

        resp = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab'
        )))
        assert resp.status_code == 400

        resp = self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            firstname='cd'
        )))
        assert resp.status_code == 400


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.app = app.test_client()

        # Create test user
        new_user = Person(
            'validuser@columbia.edu',
            'validpassword',
            'test',
            'testerson'
        )
        db.session.add(new_user)
        db.session.commit()

        return self.app

    def tearDown(self):
        db.drop_all()

    def test_user_login(self):
        response = self.app.post('/login', data = json.dumps(dict(
            exist_email='validuser@columbia.edu',
            exist_password='validpassword'
        )))
        assert response.status_code == 200

    def test_invalid_username(self):
        response = self.app.post('/login', data = json.dumps(dict(
            exist_email='wronguser@columbia.edu',
            exist_password='validpassword'
        )))
        assert response.status_code == 400

    def test_invalid_password(self):
        response = self.app.post('/login', data = json.dumps(dict(
            exist_email='validuser@columbia.edu',
            exist_password='wrongpassword'
        )))
        assert response.status_code == 400



class EventsTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        app.config['TESTING'] = True
        app.login_manager.init_app(app)

        self.app = app.test_client()

        self.app.post('/signup', data = json.dumps(dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cd'
        )))

        self.app.post('/login', data = json.dumps(dict(
            exist_email='abc@columbia.edu',
            exist_password='passwd'
        )))


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
        db.session.add(Event({
            'id': '123',
            'datetime': '1-23-45',
            'location': 'mars',
            'group': 'columbiagroup',
            'title': 'a new event',
            'group_url': 'http://www.google.com'
        }))

        db.session.commit()

        response = self.app.get('/events',
            content_type='application/json'
        )
        data = json.loads(response.data)
        assert len(data['events']) == 1


class FavoritesTestCase(unittest.TestCase):

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        app.config.from_pyfile('test_config.py')
        db.init_app(app)
        db.create_all()

        self.app = app.test_client()

        new_user = Person(
            'asdf123@columbia.edu',
            'asdf',
            'test',
            'testerson'
        )

        db.session.add(new_user)
        db.session.add(Event({
                'id': '123',
                'datetime': '1-23-45',
                'location': 'mars',
                'group': 'columbiagroup',
                'title': 'a new event',
                'group_url': 'http://www.google.com'
            }))

        db.session.commit()

        self.app.post('/login', data = json.dumps(dict(
            exist_email='asdf123@columbia.edu',
            exist_password='asdf'
        )))

        return self.app

    def tearDown(self):
        db.drop_all()

    def test_set_unset_favorite(self):
        response = self.app.post('/favorite', data = json.dumps(dict(
            id='123'
        )))
        assert response.status_code == 200

        response = self.app.delete('/favorite', data = json.dumps(dict(
            id='123'
        )))
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
