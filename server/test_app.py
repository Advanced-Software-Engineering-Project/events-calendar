# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:47:36 2016

@author: peng
"""



from flask import Flask
import unittest
import json

from app import db, app

#from app.models import *

class TestCase(unittest.TestCase):
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


#    def tearDown(self):
#        db.drop_all()

    def test_dummy(self):
        pass

    def test_user_signup(self):
        response = self.app.post('/signup', data = dict(
            email='abc@columbia.edu',
            password='passwd',
            lastname='ab',
            firstname='cc'
            #follow_redirects=True,
            #content_type='application/json'
        ))
        self.assert_equal(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()