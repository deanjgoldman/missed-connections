# -----------------
# Get post content
# -----------------
import scrapy
import sqlite3
import re
import os
import datetime
from scrapy_splash import SplashRequest
from craigslist.items import CraigslistContent

today = datetime.datetime.today().strftime('%Y-%m-%d')
db_path = os.path.join(os.path.expanduser("~"), "craigslist/craigslist/app.db")

class MySpider(scrapy.Spider):
    name = "content"
    #lines = open("links_" + str(today) + ".txt", "r").readlines()
    #start_urls = [line.split(",,,")[-1].strip() for line in sql_query]
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    sql_query = cursor.execute("SELECT url FROM links;")
    start_urls = [line[0] for line in sql_query]
    print(start_urls)
    db.close()
    
    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html')

    def parse(self, response):

        content = CraigslistContent()
        # --------------------------------------------------- 
        # dict insertion order matters

        # scrape date
        content["scrape_date"] = today

        # body
        try:
            text  = " ".join([c.strip() for c in response.xpath('//*[@id="postingbody"]/text()').extract()])
            text = re.sub(r"^u['\"]","", text)
            text = re.sub(r"[;'\"]", "", text)
            content["body"] = text
            print(content["body"])
        except:
            content["body"] = "NA"
        # --------------------------------------------------- 

        yield content
