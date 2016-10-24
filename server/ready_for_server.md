# Environment Setup
#### Step 1: PostgresSQL (9.5)
A Postgres database with a database user must be created before server runs, at localhost (127.0.0.1) through default port. As suggested in "config.py", the postgres commands are:

```sql
create user "ase4156" with password 'dbpass' nocreatedb;
create database "eventscalendar" with owner = "ase4156";
```
#### Step 2: Other Requirements
Run the following shell command to install the Python-related packages including the updated Flask, psycopg2, SQLAlchemy, etc.
```
pip install -r requirements.txt
```

