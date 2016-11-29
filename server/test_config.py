"""
flask_sqlalchemy: test_config.py
"""
SQLALCHEMY_DATABASE_URI = "postgresql://ase4156:dbpass@0.0.0.0/testeventscalendar"
#Flask-SQLAlchemy will log all the statements issued to stderr
SQLALCHEMY_ECHO = False
#Flask-SQLAlchemy will track modifications of objects and emit signals.
SQLALCHEMY_TRACK_MODIFICATIONS = True
#Testing
TESTING = True