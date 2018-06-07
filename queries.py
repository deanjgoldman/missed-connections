import re
import os
import psycopg2
from craigslist.psql import conn

class MissedConnections():
    def __init__(self):
        self.db = conn
        self.cursor = conn.cursor()
        self.content = self.load()

    def load(self):
        self.cursor.execute("SELECT body FROM content;")
        return [line[0] for line in self.cursor.fetchall()]

