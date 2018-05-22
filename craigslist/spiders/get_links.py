# ----------
# Get links
# ----------
import datetime
import scrapy
from scrapy_splash import SplashRequest
from craigslist.items import CraigslistItem


today = datetime.datetime.today().strftime('%Y-%m-%d')

class MySpider(scrapy.Spider):
    name = "links"
    numbers = [0, 120, 240]
    base_url = "https://newyork.craigslist.org/search/mis?s="
    start_urls = [str(base_url + str(num)) for num in numbers]

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield SplashRequest(url=url,
                                callback=self.parse,
                                endpoint='render.html')

    def parse(self, response):
        item = CraigslistItem()
        for i in range(1, 121):
            try:
                # dict insertion order matters
                # --------------------------------------------------------------
                # scrape date
                item["scrape_date"] = today
                # post date
                i = str(i)
                date = '//*[@id="sortable-results"]/ul/li[' + i + ']/p/time/text()'
                item['post_date'] = str(response.xpath(date).extract()[0])
                # text
                text = '//*[@id="sortable-results"]/ul/li[' + i + ']/p/a/text()'
                item["text"] = str(response.xpath(text).extract()[0])
                # url
                new_url = str(response.xpath('//*[@id="sortable-results"]/ul/li[' + i + ']/p/a/@href').extract()[0])
                item["url"] = new_url
                # location
                location = '//*[@id="sortable-results"]/ul/li[' + i + ']/p/span[3]/span[1]/text()'
                try:
                    item['location'] = str(response.xpath(location).extract()[0])
                except:
                    item["location"] = "NA"
                # --------------------------------------------------------------
                yield item

            except IndexError:
                break
