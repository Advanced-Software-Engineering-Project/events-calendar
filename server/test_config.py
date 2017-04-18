"""
flask_sqlalchemy: test_config.py
"""
SQLALCHEMY_DATABASE_URI = "postgres://lkgexzqdavpeac:91b7e8e37f73ed5eb1043eab0ac792eda311c2f42189d8d46a0f3d5e614de311@ec2-107-20-141-145.compute-1.amazonaws.com:5432/d7e6q8v93dkcur"
#Flask-SQLAlchemy will log all the statements issued to stderr
SQLALCHEMY_ECHO = False
#Flask-SQLAlchemy will track modifications of objects and emit signals.
SQLALCHEMY_TRACK_MODIFICATIONS = True
#Testing
TESTING = True
