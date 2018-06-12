# -----------------
# Get post content
# -----------------
import scrapy
import re
import os
import datetime
from scrapy_splash import SplashRequest
from craigslist.items import CraigslistContent
import psycopg2

# Include Postgres connection settings here
DATABASE_URL = os.environ.get("DATABASE_URL")

today = datetime.datetime.today().strftime('%Y-%m-%d')

class MySpider(scrapy.Spider):
    name = "content"
    conn = psycopg2.connect(dbname=DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM links WHERE scrape_date = '{today}';".format(today=today))
    try:
        start_urls = [line[0] for line in cursor.fetchall()]
    except TypeError: # links is empty
        print("------  Bad query   --------")
        pass
    
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
