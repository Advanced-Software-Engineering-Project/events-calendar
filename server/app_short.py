# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:58:19 2016

@author: peng
"""

import os
from flask import Flask, Response, request, jsonify
#from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))
#app.config.from_pyfile('config.py')
#db = SQLAlchemy(app)

   
#######


@app.route('/')
def hello():
    return "Hello Index!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
@app.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
	print(request.data)
	return jsonify(user_id=123)

@app.route('/login', methods=['POST', 'OPTIONS'])
def login():
	print(request)
	return "error"




# Temporary local development solution for CORS
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response




if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)
