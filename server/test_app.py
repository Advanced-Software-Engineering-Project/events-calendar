# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:47:36 2016

@author: peng
"""

import os
from app import app, init_config, init_db
import unittest

import tempfile


class TestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        db = init_db(app, True)
        db.create_all()


        # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        # with app.app_context():
        #     app.init_db()


    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)



    def test_signup(self):
        return self.app.post('/signup', data = dict(
                email='abc@columbia.edu',
                password='passwd',
                lastname='ab',
                firstname='cc'
            #follow_redirects=True,
            #content_type='application/json'
        ))

if __name__ == '__main__':
    unittest.main()