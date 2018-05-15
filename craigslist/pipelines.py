# -*- coding: utf-8 -*-
import datetime

today = datetime.datetime.today().strftime('%Y-%m-%d')


class CraigslistPipeline(object):
    def __init__(self):
        self.filename = "links_" + str(today) + ".txt"

    def open_spider(self, spider):
        self.file = open(self.filename, "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print(str("-"*25) + " IN PIPELINE " + str("-"*25))
        line = item["text"] + ",,," + item['date'] + ",,," + item['location'] + ",,," + item["url"] + "\n"
        self.file.write(line)
        return item


class CraigslistContentPipeline(object):

    def __init__(self):
        self.filename = "craigslist_content_" + str(today) +  ".txt"

    def open_spider(self, spider):
        self.file = open(self.filename, "a")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, content, spider):
        print(str("-"*25) + " IN CONTENT PIPELINE " + str("-"*25))
        self.file.write(content["body"] + "\n")
        return content
