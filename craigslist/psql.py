import os
import psycopg2

# Include Postgres connection settings here
USER = os.environ.get("USER")
DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(dbname=DATABASE_URL)
