# Columbia Events Calendar

[![Build Status](https://travis-ci.org/Advanced-Software-Engineering-Project/events-calendar.svg?branch=master)](https://travis-ci.org/Advanced-Software-Engineering-Project/events-calendar)

http://columbia-events-calendar.herokuapp.com

## In repository
* Scripts:
```
/server
/scraper
/webapp
clock.py
fabfile.py
```

* Test cases: `/server/test_app.py`
* Configuration files:`/server/config.py`
* Data sets: 
```
/scraper/data
psql eventscalendar -U ase4156 -h 35.185.1.150
```

* Reports:
  * [Black-box tests](https://github.com/Advanced-Software-Engineering-Project/events-calendar/wiki/Black-Box-Test-Cases)
  * White-box static tests: `/static_analysis_report` and `/code_inspection_report`
  * White-box dynamic tests: coverage report `/server/htmlcov` and [system tests](https://github.com/Advanced-Software-Engineering-Project/events-calendar/wiki/Full-System-Test)

## Introduction

There are many groups on Facebook that are associated with Columbia University, which makes it difficult for a user to search through all of the available events to find one that they might be interested in. Our hypothesis is that a unified event calendar of all Columbia events would make it easier for students, faculty and staff to find such events, based on key search terms, or a specific date and time. 
  
The Columbia Events Calendar will be focused around a visual calendar of events aggregated from the Facebook API along with facebook groups within the Columbia University community. This program will allow users to quickly view and obtain details about an event’s location, date, time, and hosts. Additionally, it will provide users with the ability to search and filter through events by date, location, and organization/host. A user will also be able to leave ratings on past events that are tied to their profile. These events’ ratings will be used to calculate an average rating for the group that they were posted by, which will give users a better suggestion of the groups and events which they might want to attend in the future. 

## Technology

* Frontend: HTML, JS, Bootstrap
* Backend: Postgres, Python, Flask, SQLAlchemy

## Running the Web Application

#### Step 1: Setup Python and Postgres

Run the following shell command to install:
* Python 2.7.11 or above
* Python pip 8 or above
* Postgresql 9.3 or above
* Postgresql Server 9.3 or above
```
sudo apt-get install python-dev python-pip postgresql-9.3 postgresql-server-dev-9.3
```

#### Step 2: Setup Python Package Requirements

Run the following shell command to pip install the Python packages including the updated psycopg2, SQLAlchemy, Flask, Flask-sqlalchemy, Flask-login.
```
sudo pip install -r requirements.txt
```

#### Step 3: Run it

```
cd server
python app.py
```
Now, the application is available on `localhost:5000`

Or you could use
```
cd server
python app.py 0.0.0.0 8111 --threaded
```
Now, the application is available on `0.0.0.0:8111` running in a optimized threaded way.

Or please visit http://columbia-events-calendar.herokuapp.com
