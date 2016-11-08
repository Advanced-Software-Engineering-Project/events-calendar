# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:47:36 2016

@author: peng
"""

import os
import app
import unittest

from flask import json, jsonify

class TestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

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