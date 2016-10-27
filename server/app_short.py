# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:58:19 2016

@author: peng
"""

import os
from flask import Flask, Response, request, jsonify, render_template
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder='../webapp/login/',
            template_folder='../webapp/login/')
#app.add_url_rule('/', 'root', lambda: app.send_static_file('../webapp/login/index.html'))
#app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)

   
#######


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
@app.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
	print(request.data)
	return jsonify(user_id=4)

@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
	print(request)
	return jsonify(user_id=456)

@app.route('/events', methods=['GET', 'OPTIONS'])
def events():
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




# Temporary local development solution for CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response




if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)
