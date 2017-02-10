"""
flask_sqlalchemy: config.py
"""
SQLALCHEMY_DATABASE_URI = "
postgres://uxrqheianbljra:c21d477cbd7c186d52fba593f484e9e6862a925f3b1bd81c6f7896d06c7a8dc7@ec2-54-235-120-39.compute-1.amazonaws.com:5432/dd1hom7cbd6tgk"
#Flask-SQLAlchemy will log all the statements issued to stderr
SQLALCHEMY_ECHO = True
#Flask-SQLAlchemy will track modifications of objects and emit signals.
SQLALCHEMY_TRACK_MODIFICATIONS = True
