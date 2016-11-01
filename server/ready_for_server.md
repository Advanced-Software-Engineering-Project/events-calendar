# Environment Setup
#### Step 1: Python and Postgres
Run the following shell command to install:
* Python 2.7.11 or above
* Python pip 8
* Postgresql 9.3 or above
* Postgresql Server 9.3 or above
```
sudo apt-get install python-dev python-pip postgresql-9.3 postgresql-server-dev-9.3
```

#### Step 2: Other Requirements
Run the following shell command to install the Python packages using `pip` including the updated Flask, psycopg2, SQLAlchemy, etc.
```
sudo pip install -r requirements.txt
```

#### Step 3: Run it
After changing directory to `/server`, run
```
python app.py
```
Now, the application is available on `localhost:5000`

