# -*- coding: utf-8 -*-
import datetime
import psycopg2
import os
from psql import conn

today = datetime.datetime.today().strftime('%Y-%m-%d')

class CraigslistPipeline(object):
    def __init__(self):
        self.table = "links"
        self.columns = {"scrape_date":"TEXT", "post_date":"TEXT", "text":"TEXT", "url":"TEXT", "location":"TEXT"}

    def open_spider(self, spider):
        self.db = conn
        create = "CREATE TABLE IF NOT EXISTS {}({});".format(self.table, ", ".join((" ".join(row) for row in self.columns.items())))
        self.db.cursor().execute(create)
    
    def close_spider(self, spider):
        self.db.commit()
        self.db.close()

    def process_item(self, item, spider):
        print(str("-"*25) + " IN PIPELINE " + str("-"*25))
        try:
            insert = "INSERT INTO {} VALUES('{}');".format(self.table, "', '".join(item.values()))
            self.db.cursor().execute(insert)
        except:
            self.db.cursor().execute("ROLLBACK");
            pass
        return item


class CraigslistContentPipeline(object):

    def __init__(self):
        self.table = "content"
        self.columns = {"scrape_date":"TEXT", "body":"TEXT"}

    def open_spider(self, spider):
        self.db = conn
        create = "CREATE TABLE IF NOT EXISTS {}({});".format(self.table, ", ".join((" ".join(row) for row in self.columns.items())))
        self.db.cursor().execute(create)

    def close_spider(self, spider):
        self.db.commit()
        self.db.close()

    def process_item(self, item, spider):
        print(str("-"*25) + " IN CONTENT PIPELINE " + str("-"*25))
        try:
            insert = "INSERT INTO {} VALUES('{}');".format(self.table, "', '".join(item.values()))
            self.db.cursor().execute(insert)
        except:
            self.db.cursor().execute("ROLLBACK");
            pass
        return item


