# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:58:19 2016

@author: peng
"""

import os
from flask import Flask, Response
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))
app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)

   
#######


@app.route('/')
def hello():
    return "Hello Index!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
@app.route('/signup')
def signup(email, password):
    return Response('success')

@app.route('/login')
def login(email, password):
    return Response('success')


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)