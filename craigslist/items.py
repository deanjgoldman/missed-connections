# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CraigslistItem(scrapy.Item):
    text = scrapy.Field()
    post_date = scrapy.Field()
    scrape_date = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()


class CraigslistContent(scrapy.Item):
    scrape_date = scrapy.Field()
    body = scrapy.Field()
