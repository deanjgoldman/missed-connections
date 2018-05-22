import re
import os
import sqlite3
from ast import literal_eval

db_path = os.path.join(os.path.expanduser("~"), "craigslist/craigslist/app.db")

class MissedConnections():
    def __init__(self):
        self.db = sqlite3.connect(db_path)
        self.content = self.load()

    def load(self):
        sql_query = self.db.cursor().execute("SELECT body FROM content;")
        return [line[0] for line in sql_query]

