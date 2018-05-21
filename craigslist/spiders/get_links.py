# Get links
import scrapy
from scrapy_splash import SplashRequest
from craigslist.items import CraigslistItem
import csv


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
        with open("links.csv", 'a') as myfile:
            for i in range(1, 121):
                try:
                    i = str(i)
                    text = '//*[@id="sortable-results"]/ul/li[' + i + ']/p/a/text()'
                    item["text"] = str(response.xpath(text).extract()[0])
                    date = '//*[@id="sortable-results"]/ul/li[' + i + ']/p/time/text()'
                    item['date'] = str(response.xpath(date).extract()[0])
                    location = '//*[@id="sortable-results"]/ul/li[' + i + ']/p/span[3]/span[1]/text()'
                    try:
                        item['location'] = str(response.xpath(location).extract()[0])
                    except:
                        item["location"] = "NA"
                    new_url = str(response.xpath('//*[@id="sortable-results"]/ul/li[' + i + ']/p/a/@href').extract()[0])
                    item["url"] = new_url
                    w = csv.DictWriter(myfile, item.keys(), delimiter="\t")
                    w.writerow(item)
                    yield item
                except IndexError:
                    break
