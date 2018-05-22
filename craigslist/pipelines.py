# -*- coding: utf-8 -*-
import datetime
import sqlite3
import os

today = datetime.datetime.today().strftime('%Y-%m-%d')

db_path = os.path.join(os.path.expanduser("~"), "craigslist/craigslist/app.db")

class CraigslistPipeline(object):
    def __init__(self):
        #self.filename = "links_" + str(today) + ".txt"
        self.table = "links"
        self.columns = {"scrape_date":"TEXT", "post_date":"TEXT", "text":"TEXT", "url":"TEXT", "location":"TEXT"}

    def open_spider(self, spider):
        #self.file = open(self.filename, "w")
        self.db = sqlite3.connect(db_path)
        #create = "CREATE TABLE IF NOT EXISTS links({0} TEXT, {1} TEXT, {2} TEXT, {3} TEXT);".format(*columns.keys())
        #create = "CREATE TABLE IF NOT EXISTS {}({}, {}, {}, {});".format(self.table, *(" ".join(row) for row in columns.items()))
        create = "CREATE TABLE IF NOT EXISTS {}({});".format(self.table, ", ".join((" ".join(row) for row in self.columns.items())))
        self.db.cursor().execute(create)
    
    def close_spider(self, spider):
        #self.file.close()
        self.db.commit()
        self.db.close()

    def process_item(self, item, spider):
        print(str("-"*25) + " IN PIPELINE " + str("-"*25))
        #line = item["text"] + ",,," + item['date'] + ",,," + item['location'] + ",,," + item["url"] + "\n"
        #self.file.write(line)
        #create = "INSERT INTO {}('{}') VALUES('{}')".format(self.table, ", ".join(item.keys()), ", ".join(item.values()))
        insert = "INSERT INTO {} VALUES('{}')".format(self.table, "', '".join(item.values()))
        self.db.cursor().execute(insert)
        return item


class CraigslistContentPipeline(object):

    def __init__(self):
        #self.filename = "craigslist_content_" + str(today) +  ".txt"
        self.table = "content"
        self.columns = {"scrape_date":"TEXT", "body":"TEXT"}

    def open_spider(self, spider):
        #self.file = open(self.filename, "a")
        self.db = sqlite3.connect(db_path)
        #create = "CREATE TABLE IF NOT EXISTS {}({});".format(self.table, *(" ".join(row) for row in columns.items()))
        create = "CREATE TABLE IF NOT EXISTS {}({});".format(self.table, ", ".join((" ".join(row) for row in self.columns.items())))
        self.db.cursor().execute(create)

    def close_spider(self, spider):
        #self.file.close()
        self.db.commit()
        self.db.close()

    def process_item(self, item, spider):
        print(str("-"*25) + " IN CONTENT PIPELINE " + str("-"*25))
        #self.file.write(item["body"] + "\n")
        #self.cursor.execute("INSERT INTO content('{}') VALUES('{}')".format(*item.keys(), *item.values())) 
        #create = "INSERT INTO {}('{}') VALUES('{}')".format(self.table, ", ".join(item.keys()), ", ".join(item.values()))
        insert = "INSERT INTO {} VALUES('{}')".format(self.table, "', '".join(item.values()))
        self.db.cursor().execute(insert)
        return item


