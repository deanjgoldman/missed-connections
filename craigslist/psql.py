import os
import psycopg2

# Include Postgres connection settings here

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
