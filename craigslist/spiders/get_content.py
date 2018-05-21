# Get post content
import scrapy
import datetime
# from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest
from craigslist.items import CraigslistContent

today = datetime.datetime.today().strftime('%Y-%m-%d')

class MySpider(scrapy.Spider):
    name = "content"
    lines = open("links_" + str(today) + ".txt", "r").readlines()

    start_urls = [line.split(",,,")[-1].strip() for line in lines]

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html')

    def parse(self, response):
        content = CraigslistContent()
        try:
            content['body'] = str(response.xpath('//*[@id="postingbody"]/text()').extract())
            print(content["body"])
        except:
            content["body"] = "NA"
        yield content
