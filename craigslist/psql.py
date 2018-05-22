import os
import psycopg2

USER = os.environ.get("USER")
DATABASE_URL = os.environ.get("DATABASE_URL")

#conn = psycopg2.connect(dbname="mc", user="deangoldman", host="localhost")
conn = psycopg2.connect(dbname="mc", user="deangoldman", host="/tmp/")#, sslmode="require")
#cursor = conn.cursor()
#cursor.execute("SELECT url FROM links;")
#test = cursor.fetchall()
#for row in test:
#    print(row)
